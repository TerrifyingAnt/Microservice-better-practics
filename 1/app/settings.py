from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    amqp_url: str = "amqp://guest:guest123@51.250.26.59:5672"
    postgres_url: str = "postgresql://postgres:postgres@postgres:5432/orderservice_db"
    port: str = "80"


settings = Settings()