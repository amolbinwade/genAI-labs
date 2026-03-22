# Incident Classification Engine

A prompt-based genAI-driven incident classification engine that uses large language models to classify incident reports into structured categories.

## Overview

This application uses generative AI models to classify incident descriptions with structured outputs.

### Technical Features
- **Rate Limiting**: Custom in-memory rate limiter using Python's threading.Lock, allowing one request per minute per client to prevent abuse.
- **Input Validation**: Pydantic models for request validation, including character limits (max 1000 characters for input text).
- **Output Format**: Structured JSON responses using Pydantic models, including token counts and response times.
- **Tech Stack**: Built with Python, FastAPI for the API framework, Google Gemini AI for classification, and Docker for containerization.

## Project Structure

- `app/` - Main application code
  - `main.py` - Application entry point
  - `api/` - API routes and endpoints
  - `core/` - Core configuration and settings
  - `models/` - Request and response models
  - `services/` - Business logic and service layer

## Requirements

See `requirements.txt` for all dependencies and their versions.

## Local Setup Instructions

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start project

```bash
cd projects/02_incident_classification_engine
uvicorn app.main:app --reload
```

## Docker Usage

### Build the Docker Image

```bash
docker build -t incident-classification-engine .
```

### Run the Docker Container

```bash
docker run -d \                                        
  --name incident-classification-engine \
  -p 8000:8000 \
  -e GEMINI_API_KEY="<YOUR_GEMINI_API_KEY>" \
  -e MODEL_NAME="<GEMINI_LLM_MODEL_NAME>" \
  amolbinwade/incident-classification-engine:latest
```

The application will be available at `http://localhost:8000`.

### Stop the Docker Container

Find the running container:

```bash
docker ps
```

Stop the container using its ID:

```bash
docker stop <container_id>
```

## Deployment to Google Cloud Platform

### Step#1.1: Build docker image supported on GCP
```
docker buildx build \
  --platform linux/amd64 \
  -t amolbinwade/incident-classification-engine:latest .
  ```

### Step#1.2: Install GCP CLI
```brew install --cask google-cloud-sdk```

### Step#2: Enable required GCP services
```
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable secretmanager.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Step#3: Install components
```
gcloud components install kubectl
```

### Step#4: Create docker repo
```
gcloud artifacts repositories create genai-labs-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker repo for genai-labs analyzer"
  ```

### Step#5: Tag Your Docker Image for GCP

```
docker tag amolbinwade/incident-classification-engine:latest \
us-central1-docker.pkg.dev/<PROJECT_ID>/genai-labs-repo/incident-classification-engine:latest
```

### Step#6: Push docker image to GCP docker repo

```
docker push \
us-central1-docker.pkg.dev/<PROJECT_ID>/genai-labs-repo/incident-classification-engine:latest
```

### Step#7: Create Gemini API secret
```
echo -n "<YOUR_GEMINI_API_KEY>" | \
gcloud secrets create gemini-api-key \
--data-file=-
  ```
### Step#8: Grant cloud run permission to read api key
```
gcloud secrets add-iam-policy-binding gemini-api-key \
  --member="serviceAccount:$(gcloud projects describe <PROJECT_ID> --format='value(projectNumber)')-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
  ```
### Step#9: Run docker container in GCP Run service

```
gcloud run deploy incident-classification-engine \
  --image us-central1-docker.pkg.dev/<PROJECT_ID>/genai-labs-repo/incident-classification-engine:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8000 \
  --cpu 0.5 \
  --memory 256Mi \
  --max-instances 1 \
  --concurrency 1 \
  --set-secrets GEMINI_API_KEY=gemini-api-key:latest \
  --set-env-vars MODEL_NAME=gemini-2.5-flash
  ```

### Step#10 : Delete service when not in use
```
gcloud run services delete incident-classification-engine --region us-central1
```
