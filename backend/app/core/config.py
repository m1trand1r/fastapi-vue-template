import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = ''
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20
    DATABASE_URL: str = ''

settings = Settings()