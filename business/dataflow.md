# dataflow.md  

## System Dataflow Architecture for **PromptForge**

```
+-------------------+        +-------------------+        +-------------------+
|   External Data   |        |   Ingestion Layer |        |   Processing /    |
|   Sources         |        |   (API Gateway)   |        |   Transform Layer |
|-------------------|        |-------------------|        |-------------------|
| • OpenAI / Anthro│  -->   | • AuthN / AuthZ   |  -->   | • Prompt Parser   |
|   pic AI APIs     |        | • Rate Limiter    |        | • Test Runner     |
| • HuggingFace Hub |        | • Validation      |        | • Metric Engine   |
| • Custom Model    |        | • Queue (Kafka)   |        | • Result Normal‑ |
|   Endpoints       |        |                   |        |   ization         |
+-------------------+        +-------------------+        +-------------------+
          |                           |                           |
          v                           v                           v
+-------------------+        +-------------------+        +-------------------+
|   Storage Tier    |<-------|   Query / Serve   |<-------|   Egress to User  |
|-------------------|        |   Layer (API)     |        |   (Web UI / CLI) |
| • Raw Prompt DB   |  <--   | • AuthN / AuthZ   |  <--   | • AuthN / AuthZ   |
|   (PostgreSQL)    |        | • Cache (Redis)   |        | • Rate Limiter    |
| • Test Results DB |        | • GraphQL / REST  |        | • Download / API  |
|   (ClickHouse)    |        |   Endpoints       |        |   Export          |
| • Artifact Store  |        +-------------------+        +-------------------+
|   (S3/MinIO)      |
+-------------------+
```

---

### 1. External Data Sources
- **LLM Provider APIs** – OpenAI, Anthropic, Cohere, Azure OpenAI, etc. (REST/HTTPS)
- **Model Hub** – HuggingFace model repository (model binaries, config)
- **User‑provided Models** – Private endpoints (on‑prem or cloud VMs) reachable via secure TLS
- **Benchmark Datasets** – Public prompt‑evaluation datasets (e.g., BIG‑Bench, HELM) stored in S3 buckets
- **Telemetry / Logging** – CloudWatch, Datadog streams for observability (optional)

### 2. Ingestion Layer
| Component | Responsibility | Tech / Notes |
|-----------|----------------|--------------|
| **API Gateway** (e.g., Kong, AWS API GW) | Single entry point, TLS termination, request routing | Enforces OAuth2 / OIDC |
| **AuthN / AuthZ** | Validate JWTs, map to roles (admin, researcher, dev) | RBAC policies stored in Keycloak |
| **Rate Limiter** | Prevent abuse of LLM provider quotas | Token bucket per tenant |
| **Request Validator** | Schema validation of prompt test definitions (JSON‑Schema) | FastAPI / Pydantic |
| **Message Queue** | Decouple ingestion from processing; back‑pressure handling | Apache Kafka (topic: `prompt_jobs`) |
| **Audit Logger** | Immutable log of all ingestion events | Write‑once S3 bucket |

### 3. Processing / Transform Layer
| Component | Responsibility | Tech / Notes |
|-----------|----------------|--------------|
| **Prompt Parser** | Normalizes, tokenizes, extracts variables | spaCy + custom tokenizer |
| **Test Runner Workers** | Executes prompts against selected LLMs, captures raw completions | Dockerized workers, GPU optional, concurrency controlled via Celery + Redis |
| **Metric Engine** | Computes evaluation metrics (BLEU, ROUGE, Exact‑Match, custom rubric) | Python‑pandas, NumPy, optional GPU acceleration |
| **Result Normalizer** | Aligns outputs to a canonical schema, adds timestamps, provenance | Avro schema enforcement |
| **Orchestrator** | Coordinates multi‑step pipelines, retries, error handling | Airflow / Prefect DAGs |
| **Security Sandbox** | Isolates untrusted model endpoints (network policies, seccomp) | gVisor or Firecracker micro‑VMs |

### 4. Storage Tier
- **Raw Prompt DB** – PostgreSQL (JSONB) – stores user‑submitted prompts, metadata, versioning.
- **Test Results DB** – ClickHouse – columnar store optimized for analytical queries on large result sets.
- **Artifact Store** – MinIO (S3‑compatible) – stores raw model responses, logs, generated reports (PDF/HTML).
- **Metadata Index** – Elasticsearch – full‑text search over prompts, tags, and evaluation notes.
- **Backup / DR** – Daily snapshots to a separate region (AWS S3 Glacier).

### 5. Query / Serving Layer
| Component | Responsibility | Tech / Notes |
|-----------|----------------|--------------|
| **AuthN / AuthZ** (re‑checked) | Enforce per‑tenant data isolation | JWT scopes |
| **Cache** – Redis | Frequently accessed result sets, leaderboard snapshots | TTL 5 min |
| **API Service** – FastAPI | GraphQL & REST endpoints for: <br>• Prompt CRUD <br>• Test job status <br>• Metric queries <br>• Export reports | OpenAPI spec |
| **Analytics Engine** | Aggregations, percentile calculations, A/B test comparisons | ClickHouse SQL + materialized views |
| **WebSocket / SSE** | Real‑time job progress updates to UI | FastAPI background tasks |
| **Rate Limiter** | Protect downstream LLM quota usage from UI‑driven loops | Token bucket per user |

### 6. Egress to User
- **Web UI** (React + Vite) – Dashboard, prompt editor, result visualizer, export buttons.
- **CLI** (`promptforge-cli`) – Submit jobs, poll status, download CSV/JSON reports.
- **Export APIs** – Generate downloadable artifacts (CSV, JSON, PDF) via signed URLs (S3 pre‑signed).
- **Notification Service** – Email / Slack webhook on job completion or failure (via AWS SNS).
- **Auth Boundary** – All egress endpoints require valid JWT; short‑lived signed URLs for artifact download.

---

### Security & Compliance Highlights
- **Zero‑Trust**: Every tier validates JWTs; no implicit trust between layers.
- **Network Segmentation**: Ingestion, processing, and storage run in separate VPC subnets with strict security groups.
- **Data Encryption**: TLS‑1.3 in‑flight; at‑rest AES‑256 for DBs and object store.
- **Audit Trail**: Immutable logs stored in WORM‑enabled bucket; searchable via Athena.
- **GDPR / CCPA**: User data flagged with `personal_data` tag; automatic purge after configurable retention (default 90 days).

--- 

*End of dataflow.md*