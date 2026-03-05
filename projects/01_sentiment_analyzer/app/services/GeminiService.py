import logging

import google.generativeai as genai
import json
import re
from app.core.config import settings
from app.models.Response import Response
from app.core.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiService:

    def _extract_json(self, text: str) -> dict:
        """
        Extract JSON from text, handling markdown code blocks.
        
        Args:
            text: Raw text response from LLM
            
        Returns:
            Parsed JSON object as dictionary
        """
        
        logging.debug(f"Raw LLM response: {text}")
        # Remove markdown code blocks (```json ... ```)
        cleaned = re.sub(r'```(?:json)?\s*\n?', '', text).strip()
        
        # Try to parse the JSON
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            # If parsing fails, raise an error with the text
            raise ValueError(f"Failed to parse JSON response: {text}")

    def generate_response(self, review_text: str) -> Response:
        """
        Generate sentiment analysis for a product review.
        
        Args:
            review_text: The product review text to analyze
            
        Returns:
            Response object containing the sentiment analysis JSON
        """
        # Sanitize review text - escape special characters
        sanitized_review = review_text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', '')
        
        # Construct the full prompt with system instructions and user template
        user_prompt = USER_PROMPT_TEMPLATE.format(review_text=sanitized_review)
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        
        model = genai.GenerativeModel(settings.MODEL_NAME)
        response = model.generate_content(full_prompt)
        
        # Extract and parse JSON from response
        json_response = self._extract_json(response.text)
        
        return Response(
            response=json_response,
            prompt_tokens=response.usage_metadata.prompt_token_count,
            response_tokens=response.usage_metadata.candidates_token_count,
            response_time=0.0
        )