from fastapi import FastAPI
from app.api.v1.routes import router as llm_router

app = FastAPI(title="FastAPI Gemini Service")

app.include_router(llm_router)

@app.get("/health")
def health():
    return {"status": "UP"}