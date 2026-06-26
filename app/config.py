import json
from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openrouter_api_key: str
    openrouter_model: str = "gpt-oss-120b:free"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    cors_origins: list[str] = ["http://localhost:5173"]

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [origin.strip() for origin in v.split(",")]
        return v

    model_config = {"env_file": ".env"}


settings = Settings()
