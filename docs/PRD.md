```markdown
# Product Requirements Document (PRD.md)
## Product: promptforge
**Version:** 0.1.0
**Owner:** Senior Product/Engineering Lead
**Date:** 2026-05-23
---

## 1. Problem Statement
Large Language Model (LLM) prompt engineering remains ad-hoc, manual, and time-intensive. Teams building AI-driven applications lack:
1. **Reproducible testing** for prompt variation effects on model outputs.
2. **Automated validation** of prompt edge cases (e.g., malicious input, low-resource context).
3. **Cross-model comparability** of prompt efficacy (e.g., how Mistral vs. LLaMA respond).
4. **Cost/time savings** in prompt iteration cycles—especially for regulated or safety-critical domains.

*Existing deficits:*
- No unified tooling for systematic prompt evaluation.
- Manual log analysis and A/B testing are brittle and unscalable.
- Most prompt libraries (e.g., LangChain’s `PromptTemplate`) focus on *composition* over *evaluation*.

*Competitive gap:*
Competitors (e.g., Promptfoo, TruLens) are closed-source, pricing_models="pay-per-api-call", limiting open research. **promptforge provides open-source, local-first benchmarking with pluggable models and datasets.**

---

## 2. Target Users & Use Cases
| Segment | Use Case | Frequency | Pain Point |
|---|---|---|---|
| Startups (AI-native) | Iterate prompts before deploying vLLM/SGLang engines | Daily | Need reproducible evals before production |
| Research Labs | Compare fine-tuned LLMs on custom prompts | Weekly | No unified framework for prompt sensitivity analysis |
| DevOps / SecOps | Validate prompt resiliency to jailbreak/edge cases | Ad-hoc | Manual regex-based testing fails at scale |
| Product Managers | Rate prompts by cost/latency/accuracy | Monthly | Need decision-grade metrics |

---

## 3. Goals & Non-Goals

| **Goal** | **Measurable Target** | **Success Metric** |
|---|---|---|
| **Fast prompt iteration** | Evaluate a set of 100 prompts <5 min on single GPU | Throughput ≥20 prompts/sec |
| **Cross-model comparability** | Support ≥3 distinct model families (open weights) | Model coverage list maintained in docs |
| **Safety edge-case testing** | Include ≥5 automated jailbreak scenarios per prompt set | Edge-case coverage ≥90% of top 20 red-teaming templates |
| **Cost tracking** | Log per-token cost for each generation | Cost report per evaluation batch |
| **Reproducibility** | Hash + dataset + prompt → deterministic results | SHA-256 hashes in reports |

### Non-Goals (Out of Scope)
- Hosted cloud evaluation beyond local inference.
- Model fine-tuning or training workflows.
- Native integration with proprietary model APIs (e.g., OpenAI).

---

## 4. Key Features (Prioritized)

### 4.1 Core Features (MVP)
| Feature | Description | Priority |
|---|---|---|
| **Prompt Registry** | CRUD for prompts (tags: domain, temperature, source) | Must |
| **Dataset Hub** | Load prompts + responses from `.jsonl` or HuggingFace Datasets (license: Apache-2.0/mit) | Must |
| **Batch Evaluation** | Parallelized eval across multiple models using vLLM/SGLang on single node | Must |
| **Metric Suite** | Built-ins: BERTScore, ROUGE, Exact Match, Cost, Latency, Log Probability | Must |
| **Edge-Case Injector** | Synthetic adversarial sufixes injected into prompts (e.g., "Ignore previous instructions") | Must |
| **Reporting** | HMTL/PDF/CSV reports with diffing across prompt variants | Should |
| **CLI + SDK** | Python CLI + programmatic SDK for scripted workflows | Should |

### 4.2 Advanced (Post-MVP)
| Feature | Description | Candidate |
|---|---|---|
| **Model Swap** | Hot-swap between vLLM and SGLang backends + backends | Backlog |
| **Auto Prompt Optimization (APO)** | Use Axentx BRAIN to recommend prompt variants based on performance + cost | Future |
| **Kubernetes Operator** | Run evaluations at cluster scale with job queue + auto-scales nodes | Future |

---

## 5. Technical Requirements
| Requirement | Implementation Contract |
|---|---|
| **Models supported** | `vllm-project/vllm` (inference), `sgl-project/sglang` (structured gen) |
| **Datasets** | Auto-load from Axentx BRAIN (pgvector) for reproducible tests |
| **Licensing** | All dependencies Apache-2.0 or MIT; output datasets Apache-2.0 |
| **Scalability** | Single node 8xA100 → 200 prompts/sec |
| **Storage** | Results exported to `.jsonl` (Parquet option) |

---

## 6. Success Metrics (OKRs)
| Objective | Key Result | Baseline (goal) |
|---|---|---|
| **Performance** | Prompt eval throughput ≥20 prompts/sec | ≤10 prompts/sec (current) |
| **Quality** | Edge-case detection precision ≥0.85 (F1) | 0.65 (manual) |
| **Adoption** | ≥50 GitHub stars + 5 external forks within 3 months | 0 |
| **Cost** | Reduce prompt iteration cost by 40% vs manual workflows | 100% baseline |

---

## 7. Scope & Out of Scope

### In Scope
- MVP supports local inference only (no external APIs).
- **Supported model families**: Mistral-7B, LLaMA-3-8B, Phi-3-Mini.
- **Prompt formats**: Alpaca, Dolly, custom JSON.
- **Dataset formats**: `.jsonl`, HuggingFace Datasets (Apache-2.0).
- **CI/CD**: GitHub Actions templates for automated regression testing.

### Out of Scope
- Models requiring >32GB GPU memory (future backlog item).
- Native integration with proprietary cloud APIs (e.g., OpenAI).
- Fine-tuning loops or reinforcement learning—only evaluation.
- Web UI (CLI-first; expose REST API as v2).

---
## 8. Risks & Mitigation
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Model support skew** | High | High | Implement facade pattern for model backends; tests in CI vary model families |
| **Dataset licensing** | Medium | Medium | Only include Apache-2.0/MIT datasets; verify licenses via SPDX identifiers |
| **Security edge-case fail-open** | Low | High | Run adversarial tests in isolated sandbox; enable `--sandbox=docker` flag |

---
## 9. Success Milestones
| Phase | Deliverable | ETA |
|---|---|---|
| Alpha | MVP CLI + 5 built-in metrics + 3 edge-case templates | 2026-06-07 |
| Beta | GitHub Actions + automated regression tests + report export | 2026-06-21 |
| GA | Add APO candidate + Kubernetes operator + docs | 2026-07-19 |
```
