import time

from fastapi import APIRouter, Depends
from app.models.LLMRequest import LLMRequest
from app.models.LLMResponse import LLMResponse
from app.services.GeminiService import GeminiService
from app.core.rate_limiter import rate_limit

router = APIRouter(prefix="/llm", tags=["LLM"])
service = GeminiService()

@router.post("/generate", response_model=LLMResponse, dependencies=[Depends(rate_limit)])
def generate_text(request: LLMRequest):

    start_time = time.perf_counter()  # High precision timer
    response = service.generate_response(request.review)
    end_time = time.perf_counter()
    response_time = round(end_time - start_time, 4)  # seconds

    return LLMResponse(
        response=response.response,
        prompt_tokens=response.prompt_tokens,
        response_tokens=response.response_tokens,
        response_time=response_time,
        total_tokens=response.total_tokens()
    )
