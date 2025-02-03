FROM python:3.9-slim

# 必要なツールをインストール
RUN apt-get update && apt-get install -y curl cowsay python3-pip && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

# COW言語のインタープリタを手動でコピー
WORKDIR /app
COPY cow.py /usr/local/bin/cow.py
RUN chmod +x /usr/local/bin/cow.py

# COWスクリプトをコンテナにコピー
COPY hello.cow /app/hello.cow

# 実行コマンド
CMD ["python3", "/usr/local/bin/cow.py", "/app/hello.cow"]
