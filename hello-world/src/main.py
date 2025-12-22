import base64
import logging
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Pub/Sub メッセージのスキーマ定義
class PubSubMessage(BaseModel):
    data: str | None = None
    messageId: str | None = None
    message_id: str | None = None
    publishTime: str | None = None
    publish_time: str | None = None
    attributes: dict[str, Any] | None = None


class PubSubEnvelope(BaseModel):
    message: PubSubMessage
    subscription: str | None = None


# ルートへのアクセスで Hello, world! を返す
@app.get("/")
def read_root():
    return "Hello, world!"


# Pub/Sub Push メッセージを受け取るエンドポイント
@app.post("/error-log")
def receive_pubsub_message(envelope: PubSubEnvelope):
    """Pub/Sub からの Push メッセージを受け取り、内容をログに出力する"""
    # エンベロープ全体をログに出力
    logger.info(f"Received Pub/Sub envelope: {envelope.model_dump()}")

    # メッセージ部分を取得
    pubsub_message = envelope.message
    logger.info(f"Pub/Sub message: {pubsub_message.model_dump()}")

    # data フィールドがある場合はデコードしてログに出力
    if pubsub_message.data:
        decoded_data = base64.b64decode(pubsub_message.data).decode("utf-8")
        logger.info(f"Decoded message data: {decoded_data}")

    # subscription 情報もログに出力
    if envelope.subscription:
        logger.info(f"Subscription: {envelope.subscription}")

    return {"status": "ok"}


# error エンドポイント
@app.get("/error")
def error():
    raise Exception("test error")
