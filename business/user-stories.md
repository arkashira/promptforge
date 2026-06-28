## `user-stories.md`

### Epic 1 – Prompt Authoring & Management  
*Enable users to create, version, and organize prompts for systematic LLM testing.*

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 1.1 | **As a researcher, I want to create a new prompt template with placeholders, so that I can reuse it across multiple test cases.** | - UI form allows naming, description, and placeholder definition (e.g., `{topic}`, `{tone}`).<br>- Prompt is saved to a personal library and assigned a unique ID.<br>- Version history is automatically created on each edit.<br>- Users can clone an existing prompt to start a new one. | S |
| 1.2 | **As a developer, I want to organize prompts into folders and tag them, so that I can quickly locate relevant prompts for a project.** | - Drag‑and‑drop folder hierarchy with unlimited nesting.<br>- Multi‑tag system (e.g., `sentiment`, `code‑gen`).<br>- Search bar supports fuzzy matching on name, tags, and content.<br>- Ability to export/import a folder as JSON. | M |
| 1.3 | **As a team lead, I want to set read‑only or edit permissions on prompt folders, so that my team follows governance rules.** | - Role‑based access control (owner, editor, viewer).<br>- Permission matrix displayed per folder.<br>- Audit log records who changed permissions and when.<br>- Unauthorized users receive a clear “access denied” message. | M |
| 1.4 | **As a QA engineer, I want to bulk‑upload a CSV of prompts, so that I can seed the platform with existing test suites.** | - CSV template with columns: `prompt_id`, `template`, `placeholders`, `tags`.<br>- Validation errors highlighted with line numbers.<br>- Successful upload shows a summary (rows added/updated).<br>- Uploaded prompts inherit folder permissions of the uploader. | S |

---

### Epic 2 – Test Case Definition & Execution  
*Provide a robust framework for defining edge‑case scenarios and running them against selected LLMs.*

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 2.1 | **As a researcher, I want to define a test case with input variables and expected output patterns, so that I can automatically validate LLM behavior.** | - Test case wizard links a prompt template to a variable set (CSV/JSON).<br>- Expected output can be expressed as regex, JSON schema, or custom script.<br>- “Pass/Fail” threshold configurable (e.g., 80% regex match).<br>- Test case saved with a unique ID and versioned. | M |
| 2.2 | **As a developer, I want to select one or more LLM endpoints (e.g., OpenAI GPT‑4, Anthropic Claude) for a test run, so that I can compare model performance.** | - Dropdown lists all configured API keys/endpoints.<br>- Ability to set per‑model parameters (temperature, max tokens).<br>- Parallel execution across models with a configurable concurrency limit.<br>- Results displayed side‑by‑side in a matrix view. | M |
| 2.3 | **As a data scientist, I want to schedule recurring test runs (daily/weekly), so that I can monitor model drift over time.** | - Cron‑style scheduler UI with next‑run preview.<br>- Notification options: email, Slack webhook, in‑app alert.<br>- Historical run results retained for at least 90 days.<br>- Ability to pause/cancel scheduled jobs. | L |
| 2.4 | **As a QA engineer, I want to run a “sandbox” mode that limits token usage, so that I can test without incurring high costs.** | - Sandbox toggle caps max tokens per request and total tokens per run.<br>- Real‑time cost estimate displayed before execution.<br>- Sandbox runs are flagged in the results UI. | S |

---

### Epic 3 – Analytics, Reporting & Collaboration  
*Turn raw test outputs into actionable insights and enable team collaboration.*

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 3.1 | **As a researcher, I want a dashboard that shows pass/fail rates per model and per prompt, so that I can quickly spot weak spots.** | - Heat‑map visualization with models on X‑axis, prompts on Y‑axis.<br>- Hover tooltip shows exact pass percentage and sample failures.<br>- Ability to filter by date range, tags, or test suite.<br>- Exportable as CSV or PNG. | M |
| 3.2 | **As a product manager, I want to generate a PDF report summarizing a test run, so that I can share findings with stakeholders.** | - One‑click “Generate Report” button.<br>- Report includes executive summary, methodology, tables, and charts.<br>- Customizable cover page (logo, title, date).<br>- Downloadable PDF and shareable link with view‑only access. | M |
| 3.3 | **As a developer, I want to comment on individual test case results, so that I can discuss failures with the team.** | - Inline comment thread attached to each failed instance.<br>- @‑mention support triggers email/Slack notification.<br>- Comment history is immutable and searchable.<br>- Ability to mark a comment as “resolved”. | S |
| 3.4 | **As a data scientist, I want to export raw response logs (prompt, model output, latency, token usage) to a data lake, so that I can perform deeper offline analysis.** | - Export button offers JSONL or Parquet formats.<br>- Option to select a time window or specific test suite.<br>- Integration with S3, GCS, or Azure Blob via pre‑configured credentials.<br>- Export job status shown in a progress modal. | L |

---

### Epic 4 – Security, Compliance & Extensibility  
*Ensure the platform meets enterprise security standards and can be extended via plugins.*

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 4.1 | **As a security admin, I want all API keys to be stored encrypted at rest, so that credentials are protected.** | - Keys encrypted with AES‑256 using a KMS‑managed master key.<br>- Access to keys logged in audit trail.<br>- UI shows masked keys with “reveal” requiring re‑auth. | S |
| 4.2 | **As a compliance officer, I want data retention policies (e.g., delete logs after 30 days), so that we stay GDPR‑ready.** | - Policy editor with preset intervals (7, 30, 90 days) and custom dates.<br>- Automatic purge job runs nightly and logs deletions.<br>- Ability to request an export before deletion. | M |
| 4.3 | **As a developer, I want a plugin SDK to add custom evaluation metrics, so that I can tailor scoring to my domain.** | - SDK provides hooks: `onResponse`, `computeScore`, `storeResult`.<br>- Plugins packaged as npm modules and loaded at runtime.<br>- Sandbox execution prevents malicious code (resource limits, no network).<br>- Sample plugin repository included. | L |
| 4.4 | **As an ops engineer, I want health‑check endpoints and Prometheus metrics, so that I can monitor platform reliability.** | - `/healthz` returns overall status (OK/Degraded/Down).<br>- `/metrics` exposes request latency, error rates, and token usage per model.<br>- Alerts can be configured in Grafana/Alertmanager. | S |

---  

*All stories are scoped for the MVP of **PromptForge**. Stories marked **L** are candidates for Phase 2 if early validation shows strong demand.*