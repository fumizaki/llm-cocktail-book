FROM python:3.11.9-bookworm

WORKDIR /e2e

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
COPY ./app/e2e/pyproject.toml ./app/e2e/poetry.lock .
RUN poetry install

COPY ./app/e2e .

# Playwrightブラウザのインストール
RUN playwright install chromium && playwright install-deps

# pytestを使用する場合
CMD ["pytest", "tests"]
# playwright testコマンドを使用する場合
# CMD ["python", "-m", "playwright", "test"]