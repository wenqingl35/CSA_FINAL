from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DEEPSEEK_API_KEY: str

    DEEPSEEK_BASE_URL: str = "https://openrouter.ai/api/v1"

    DEEPSEEK_MODEL: str = "deepseek/deepseek-chat-v3.1"

    class Config:
        env_file = ".env"
settings = Settings()
