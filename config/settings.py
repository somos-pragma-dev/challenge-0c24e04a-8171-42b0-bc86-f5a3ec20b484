from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Payment API'
    API_VERSION: str = '0.1.0'
    DATABASE_URL: str

    class Config:
        env_file = '.env'

settings = Settings()