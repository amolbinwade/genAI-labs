from pydantic import BaseModel

class LLMResponse(BaseModel):
    response: str
    prompt_tokens: int
    response_tokens: int
    response_time: float
    total_tokens: int