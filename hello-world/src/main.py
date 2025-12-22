import logging

from fastapi import FastAPI, Request

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# ルートへのアクセスで Hello, world! を返す
@app.get("/")
def read_root():
    return "Hello, world!"


# Pub/Sub Push メッセージを受け取るエンドポイント
@app.post("/error-log")
def receive_pubsub_message(request: Request):
    """Pub/Sub からの Push メッセージを受け取り、内容をログに出力する"""
    body = request.json()
    logger.info(f"Received Pub/Sub message: {body}")
    return {"status": "ok"}


# error エンドポイント
@app.get("/error")
def error():
    raise Exception("test error")
