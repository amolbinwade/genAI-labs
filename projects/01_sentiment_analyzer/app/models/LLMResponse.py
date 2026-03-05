from pydantic import BaseModel
from typing import Any

class LLMResponse(BaseModel):
    response: Any  # Can be string or JSON object (dict)
    prompt_tokens: int
    response_tokens: int
    response_time: float
    total_tokens: int