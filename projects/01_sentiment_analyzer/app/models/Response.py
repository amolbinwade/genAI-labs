from dataclasses import dataclass

@dataclass
class Response:
    response: str
    prompt_tokens: int
    response_tokens: int
    response_time: float  # in seconds

    def total_tokens(self) -> int:
        """Return total tokens used."""
        return self.prompt_tokens + self.response_tokens
    
    def to_dict(self):
        data = asdict(self)
        data["total_tokens"] = self.total_tokens()
        return data