from fastapi import FastAPI

# local import
from routers import health
from variables import BASE_URI

app = FastAPI()

app.include_router(health.router, prefix=BASE_URI, tags=["health"])
