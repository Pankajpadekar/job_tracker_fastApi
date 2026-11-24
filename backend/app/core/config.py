from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

# dialect+driver://username:password@host:port/database

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Job Tracker"

    # Database settings
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = 'localhost'
    postgres_port: int = 5432

    @property
    def db_url(self) -> URL:
        return str(
            URL.create(
                drivername="postgresql+asyncpg",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host,
                port=self.postgres_port,
                database=self.postgres_db
            )
        )

# read and check the settings from the environment variables and .env file
settings = Settings()