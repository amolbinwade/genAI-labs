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
