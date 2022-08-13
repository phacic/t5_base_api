import os
import pathlib
from typing import Optional
from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR = Path(__file__).parent.parent.parent

    API_V1: str = "/api/v1"

    # docker host ip
    HOST_IP: Optional[str] = None

    MODEL_DIR = pathlib.Path.joinpath(BASE_DIR, "t5_models")


settings = Settings()
