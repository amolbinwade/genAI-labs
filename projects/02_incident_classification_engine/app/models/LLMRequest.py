from pydantic import BaseModel, Field

class LLMRequest(BaseModel):
    complaint: str = Field(
        ...,
        max_length=1000,
        description="Incident description text to classify (maximum 1000 characters)"
    )
