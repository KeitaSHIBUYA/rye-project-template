from fastapi import FastAPI

app = FastAPI()


# ルートへのアクセスで Hello, world! を返す
@app.get("/")
def read_root():
    return "Hello, world!"

# error エンドポイント
@app.get("/error")
def error():
    raise Exception("test error")
