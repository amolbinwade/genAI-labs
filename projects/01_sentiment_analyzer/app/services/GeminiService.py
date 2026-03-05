import logging
import json

from google import genai
from google.genai.types import GenerateContentConfig

from app.core.config import settings
from app.models.Response import Response
from app.core.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

        self.config = GenerateContentConfig(
            temperature=0.0,
            max_output_tokens=500,
            response_mime_type="application/json"
        )

    def generate_response(self, review_text: str) -> Response:

        user_prompt = USER_PROMPT_TEMPLATE.format(review_text=review_text)
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"

        response = self.client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=full_prompt,
            config=self.config
        )
        print(response)
        print(response.text)
        logging.info(f"LLM response: {response.text}")
        json_response = json.loads(response.text)

        return Response(
            response=json_response,
            prompt_tokens=response.usage_metadata.prompt_token_count,
            response_tokens=response.usage_metadata.candidates_token_count,
            response_time=0.0
        )