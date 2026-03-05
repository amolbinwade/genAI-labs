from pydantic import BaseModel, Field

class LLMRequest(BaseModel):
    review: str = Field(
        ...,
        max_length=1000,
        description="Product review text to analyze (maximum 1000 characters)"
    )