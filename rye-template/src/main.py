from fastapi import FastAPI

from src.routers import health
from src.variables import BASE_URI

app = FastAPI()

app.include_router(health.router, prefix=BASE_URI, tags=["health"])
