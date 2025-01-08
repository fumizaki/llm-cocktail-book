.PHONY: init-app docker-up docker-down docker-free

# rootの.envファイル作成
create_root_env:
	@if [ ! -f .env ]; then \
		cp -f .env.example .env; \
	fi

# webapiの.envファイル作成
create_webapi_env:
	@if [ ! -f ./app/webapi/.env.dev ]; then \
		cp -f ./app/webapi/.env.example ./app/webapi/.env.dev; \
	fi

# webviewの.envファイル作成
create_webview_env:
	@if [ ! -f ./app/webview/.env.dev ]; then \
		cp -f ./app/webview/.env.example ./app/webview/.env.dev; \
	fi

# rdbのdataディレクトリ作成
create_rdb_data:
	@if [ ! -d ./app/rdb/postgresql/data ]; then \
		mkdir -p ./app/rdb/postgresql/data; \
	fi

# kvsのdataディレクトリ作成
create_kvs_data:
	@if [ ! -d ./app/kvs/redis/data ]; then \
		mkdir -p ./app/kvs/redis/data; \
	fi

# vdbのdataディレクトリ作成
create_vdb_data:
	@if [ ! -d ./app/vdb/qdrant/data ]; then \
		mkdir -p ./app/rdb/qdrant/data; \
	fi

# 初期セットアップコマンド
init-app: create_root_env create_webapi_env create_webview_env create_rdb_data create_kvs_data create_vdb_data

# Dockerコンテナ起動
docker-up-dev:
	docker compose -f compose.dev.yml up -d --build

# Dockerコンテナ削除
docker-down-dev:
	docker compose -f compose.dev.yml down --rmi all

# Dockerコンテナ解放
docker-free:
	docker system prune
