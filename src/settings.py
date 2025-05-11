from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_PORT: int = 5432
    POSTGRES_HOST: str = 'localhost'
    SECRET_KEY: str = 'aa74132a4e4c31cc8beb8bff4e3db368f6d2c4b2439ac65966270de2ae5f4048'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @property
    def async_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings()

