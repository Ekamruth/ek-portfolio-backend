from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openrouter_api_key: str
    openrouter_model: str = "gpt-oss-120b:free"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    cors_origin: str = "http://localhost:5173"

    model_config = {"env_file": ".env"}


settings = Settings()
