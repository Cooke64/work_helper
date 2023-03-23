import pathlib
from typing import Any

from pydantic import BaseSettings, Field

BASE_DIRECTORY = pathlib.Path(__file__).absolute().parent.parent


class AdvancedBaseSettings(BaseSettings):
    class Config:
        allow_mutation = False
        env_file = BASE_DIRECTORY / ".env"
        env_file_encoding = "utf-8"


class BotSettings(AdvancedBaseSettings):
    TOKEN: str = Field(..., env="TOKEN")
    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: str = Field(..., env="REDIS_PORT")
    BASIC_PHOTO: str = Field(..., env="BASIC_PHOTO")
    ADMINS_ID: list[int] = Field(..., env="ADMINS_ID")
    DEBUG: str = Field(..., env="_DEBUG")

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'ADMINS_ID':
                return [int(x) for x in raw_val.split(',')]
            return cls.json_loads(raw_val)


class PostgresSettings(AdvancedBaseSettings):
    PORT: str = Field(default="5432")
    USERNAME: str = Field(default="postgres")
    PASSWORD: str = Field(default="postgres")
    DATABASE: str = Field(default="postgres")
    HOST: str = Field(default="localhost")

    class Config:
        env_prefix = "DB_"


class Settings(BotSettings, PostgresSettings):
    @property
    def DATABASE_URL(self) -> str:
        if self.DEBUG:
            return 'postgresql://postgres:12345678@localhost:5432/telegram'
        return f'postgresql://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}'

    @property
    def REDIS_HOST(self) -> str:
        if self.DEBUG:
            return 'localhost'
        return self.HOST


settings = Settings()
