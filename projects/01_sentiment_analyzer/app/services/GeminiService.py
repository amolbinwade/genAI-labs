import google.generativeai as genai
from app.core.config import settings
from app.models.Response import Response

genai.configure(api_key=settings.GEMINI_API_KEY)

class GeminiService:

    def generate_response(self, prompt: str) -> Response:

        for model in genai.list_models():
            print(model.name)
        model = genai.GenerativeModel(settings.MODEL_NAME)
        response = model.generate_content(prompt)
        return Response(response=response.text, prompt_tokens=response.usage_metadata.prompt_token_count, response_tokens=response.usage_metadata.candidates_token_count, response_time=0.0)