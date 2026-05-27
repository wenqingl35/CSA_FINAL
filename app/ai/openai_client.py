from openai import AsyncOpenAI

from app.core.config import settings


class AIClient:

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:

            cls._client = AsyncOpenAI(
                api_key=settings.DEEPSEEK_API_KEY,
                base_url=settings.DEEPSEEK_BASE_URL
            )

        return cls._client


def get_ai_client():

    return AIClient.get_client()