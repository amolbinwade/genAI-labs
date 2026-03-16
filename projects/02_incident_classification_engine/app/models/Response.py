from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Response:
    response: Any  # Can be string or JSON object (dict)
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
