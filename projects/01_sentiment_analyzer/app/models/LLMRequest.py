from pydantic import BaseModel, Field

class LLMRequest(BaseModel):
    prompt: str = Field(
        ...,
        max_length=1000,
        description="Prompt text (maximum 1000 characters)"
    )