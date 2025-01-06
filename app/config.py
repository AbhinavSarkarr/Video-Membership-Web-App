from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
from functools import lru_cache
load_dotenv()

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = "1"

class Settings(BaseSettings):
    keyspace: str = Field(..., validation_alias="ASTRADB_KEYSPACE")
    client_id: str = Field(..., validation_alias="CLIENT_ID")
    client_secret: str = Field(..., validation_alias="CLIENT_SECRET")

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
