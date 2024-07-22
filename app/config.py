from pathlib import Path

from decouple import config

DIR = Path(__file__).absolute().parent
FASTAPI_HOST = config("FASTAPI_HOST", default="localhost")
FASTAPI_PORT = config("FASTAPI_PORT", default=8080, cast=int)
DELLIN_URL = config("DELLIN_URL", default="")
DELLIN_API_KEY = config("DELLIN_API_KEY", default="")
