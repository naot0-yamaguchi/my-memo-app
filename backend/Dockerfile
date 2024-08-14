# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

# アプリケーションのファイルをコピー
COPY . .

# アプリケーションを実行
CMD ["flask", "run", "--host=0.0.0.0"]
