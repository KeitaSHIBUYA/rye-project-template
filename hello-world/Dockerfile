# ベースイメージの指定
FROM python:3.12.2-slim

# 作業ディレクトリの作成
WORKDIR /app

# 依存関係ファイルのコピー
COPY ./requirements.lock ./

# 依存関係のインストール
RUN sed -i 's/^-e file:.*/# &/' requirements.lock \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.lock

# アプリケーションのソースコードをコピー
COPY ./src ./src

# アプリケーションの起動コマンド
CMD ["python", "-m", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
