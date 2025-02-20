from fastapi import FastAPI

from src.routers import health
from src.variables import BASE_URI

app = FastAPI()


# ルートへのアクセスで Hello, world! を返す
@app.get("/")
def read_root():
    return "Hello, world"


app.include_router(health.router, prefix=BASE_URI, tags=["health"])
