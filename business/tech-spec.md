# Tech Spec: PromptForge v1
## Stack
- **Language**: Python 3.9+
- **Framework**: FastAPI 3.0+
- **Runtime**: Docker, Kubernetes (for scalability and deployment)
- **Database**: PostgreSQL 13+ (for data persistence and querying)
- **Message Queue**: RabbitMQ 3.8+ (for asynchronous task processing and communication)
- **Storage**: MinIO 5.0+ (for storing and serving large model artifacts)

## Hosting
- **Free-tier-first**: Deploy on Heroku Free (for initial development and testing)
- **Specific platforms**: AWS Elastic Beanstalk (for production-ready deployment) and Google Cloud Run (for serverless scalability)

## Data Model
- **Tables/Collections**:
  - **models**: stores information about trained Large Language Models (LLMs)
    - **id** (primary key): unique identifier for the model
    - **name**: human-readable name for the model
    - **description**: brief description of the model's capabilities
    - **created_at**: timestamp for when the model was created
    - **updated_at**: timestamp for when the model was last updated
  - **prompts**: stores information about specific instructions and prompt edge cases
    - **id** (primary key): unique identifier for the prompt
    - **model_id** (foreign key): references the model that the prompt is associated with
    - **prompt_text**: the actual prompt text
    - **created_at**: timestamp for when the prompt was created
    - **updated_at**: timestamp for when the prompt was last updated
  - **results**: stores information about the evaluation results of LLMs on specific prompts
    - **id** (primary key): unique identifier for the result
    - **prompt_id** (foreign key): references the prompt that the result is associated with
    - **model_id** (foreign key): references the model that the result is associated with
    - **result_text**: the actual result text
    - **created_at**: timestamp for when the result was created
    - **updated_at**: timestamp for when the result was last updated
- **Collections**: stores information about the evaluation results of LLMs on specific prompts
  - **id** (primary key): unique identifier for the collection
  - **name**: human-readable name for the collection
  - **description**: brief description of the collection
  - **created_at**: timestamp for when the collection was created
  - **updated_at**: timestamp for when the collection was last updated

## API Surface
- **Endpoints**:
  - **GET /models**: retrieve a list of all trained LLMs
  - **GET /models/{model_id}**: retrieve information about a specific LLM
  - **POST /models**: create a new LLM
  - **GET /prompts**: retrieve a list of all specific instructions and prompt edge cases
  - **GET /prompts/{prompt_id}**: retrieve information about a specific prompt
  - **POST /prompts**: create a new prompt
  - **GET /results**: retrieve a list of all evaluation results
  - **GET /results/{result_id}**: retrieve information about a specific result
  - **POST /results**: create a new result
  - **GET /collections**: retrieve a list of all evaluation results collections
  - **GET /collections/{collection_id}**: retrieve information about a specific collection
  - **POST /collections**: create a new collection

## Security Model
- **Authentication**: use JSON Web Tokens (JWT) for authentication and authorization
- **Secrets**: store sensitive information such as API keys and database credentials using environment variables and a secrets manager
- **IAM**: use a role-based access control (RBAC) system to manage user permissions and access to resources

## Observability
- **Logs**: use a logging framework such as Loguru to log important events and errors
- **Metrics**: use a metrics framework such as Prometheus to collect and store metrics about the application
- **Traces**: use a tracing framework such as Jaeger to collect and store traces about the application's performance

## Build/CI
- **Build**: use a build tool such as Make to automate the build process
- **CI**: use a continuous integration tool such as GitHub Actions to automate testing and deployment
- **Docker**: use Docker to containerize the application and ensure consistent deployment across environments
- **Kubernetes**: use Kubernetes to manage and orchestrate the deployment of the application in a production-ready environment