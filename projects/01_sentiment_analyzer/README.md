# Sentiment Analyzer

A prompt-based genAI-driven product review sentiment analyzer that leverages large language models to analyze and understand customer sentiments from product reviews.

## Overview

This application uses generative AI models to provide advanced sentiment analysis capabilities, extracting meaningful insights from product reviews with contextual understanding and nuanced interpretation.

## Setup Instructions

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
cd projects/01_sentiment_analyzer
uvicorn app.main:app --reload
```

## Project Structure

- `app/` - Main application code
  - `main.py` - Application entry point
  - `api/` - API routes and endpoints
  - `core/` - Core configuration and settings
  - `models/` - Request and response models
  - `services/` - Business logic and service layer

## Requirements

See `requirements.txt` for all dependencies and their versions.
