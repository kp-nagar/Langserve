from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False
    OPENAI_API_KEY: str
    OPENAI_MODEL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
