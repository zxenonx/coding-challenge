import os
from dotenv import load_dotenv
from pydantic import BaseSettings
from pathlib import Path

env_path = Path(".env")
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    """Holds the configuration variables of the project."""

    PROJECT_NAME = "Grades Dataset"
    DEBUG = True
    DATASET_URL = (
        "https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.csv?accessType=DOWNLOAD"
    )

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv(
        "POSTGRES_PASSWORD",
    )
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
