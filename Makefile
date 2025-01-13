.PHONY: init-app docker-up-dev docker-down-dev docker-up-test docker-down-test docker-free

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
	@if [ ! -f ./app/webapi/.env.test ]; then \
		cp -f ./app/webapi/.env.example ./app/webapi/.env.test; \
	fi

# webviewの.envファイル作成
create_webview_env:
	@if [ ! -f ./app/webview/.env.dev ]; then \
		cp -f ./app/webview/.env.example ./app/webview/.env.dev; \
	fi
	@if [ ! -f ./app/webview/.env.test ]; then \
		cp -f ./app/webview/.env.example ./app/webview/.env.test; \
	fi

# rdbのdataディレクトリ作成
create_rdb_data:
	@if [ ! -d ./app/rdb/postgresql/dev ]; then \
		mkdir -p ./app/rdb/postgresql/dev; \
	fi
	@if [ ! -d ./app/rdb/postgresql/test ]; then \
		mkdir -p ./app/rdb/postgresql/test; \
	fi

# kvsのdataディレクトリ作成
create_kvs_data:
	@if [ ! -d ./app/kvs/redis/dev ]; then \
		mkdir -p ./app/kvs/redis/dev; \
	fi
	@if [ ! -d ./app/kvs/redis/test ]; then \
		mkdir -p ./app/kvs/redis/test; \
	fi

# vdbのdataディレクトリ作成
create_vdb_data:
	@if [ ! -d ./app/vdb/qdrant/dev ]; then \
		mkdir -p ./app/rdb/qdrant/dev; \
	fi
	@if [ ! -d ./app/vdb/qdrant/test ]; then \
		mkdir -p ./app/rdb/qdrant/test; \
	fi

# 初期セットアップコマンド
init-app: create_root_env create_webapi_env create_webview_env create_rdb_data create_kvs_data create_vdb_data

# Dockerコンテナ起動
docker-up-dev:
	docker compose -f compose.dev.yml up -d --build

# Dockerコンテナ削除
docker-down-dev:
	docker compose -f compose.dev.yml down --rmi all

# Dockerコンテナ起動
docker-up-test:
	docker compose -f compose.test.yml up -d --build

# Dockerコンテナ削除
docker-down-test:
	docker compose -f compose.test.yml down --rmi all

# Dockerコンテナ解放
docker-free:
	docker system prune
