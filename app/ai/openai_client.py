from openai import AsyncOpenAI
from app.core.config import settings


class OpenAIClientManager:
    """
    Centralized OpenAI client manager.

    Responsibilities:
    - API key management
    - model defaults
    - future retry logic
    - future logging/tracking
    - future rate limiting
    """

    _client = None

    @classmethod
    def get_client(cls) -> AsyncOpenAI:

        if cls._client is None:
            cls._client = AsyncOpenAI(
                api_key=settings.OPENAI_API_KEY
            )

        return cls._client


def get_openai_client() -> AsyncOpenAI:
    """
    Convenience helper.
    """

    return OpenAIClientManager.get_client()