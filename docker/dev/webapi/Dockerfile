FROM python:3.11.9-bookworm

WORKDIR /webapi

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetryをダウンロードしてインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Pathを通す
ENV PATH /root/.local/bin:$PATH
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY ./app/webapi/pyproject.toml ./app/webapi/poetry.lock .
RUN poetry install

COPY ./app/webapi .

CMD ["bash", "-c", "uvicorn main:app --reload --host 0.0.0.0 --port 8000"]
# CMD ["bash", "-c", "gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000"]