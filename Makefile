.PHONY: init docker-up docker-down docker-free


# デフォルトの環境を local に設定
ENV ?= local

# rootの.envファイル作成
create_root_env:
	@if [ ! -f ./.env.example ]; then \
		echo "WEBVIEW_PORT=3000" > ./.env.example; \
		echo "WEBAPI_PORT=8000" >> ./.env.example; \
		echo "RDB_NAME=rdb" >> ./.env.example; \
		echo "RDB_USER=rdb" >> ./.env.example; \
		echo "RDB_PASSWORD=rdb" >> ./.env.example; \
		echo "RDB_PORT=5432" >> ./.env.example; \
		echo "KVS_PORT=6379" >> ./.env.example; \
		echo "VECTOR_PORT=6333" >> ./.env.example; \
		echo "GRAPH_PORT=7474" >> ./.env.example; \
	fi
	@if [ ! -f .env ]; then \
		cp -f .env.example .env; \
	fi

# webviewの.envファイル作成
create_webview_env:
	@if [ ! -f ./app/webview/.env.example ]; then \
		echo "NODE_ENV=local" > ./app/webview/.env.example; \
	fi
	@if [ ! -f ./app/webview/.env.local ]; then \
		cp -f ./app/webview/.env.example ./app/webview/.env.local; \
	fi
	@if [ ! -f ./app/webview/.env.test ]; then \
		cp -f ./app/webview/.env.example ./app/webview/.env.test; \
	fi


# webapiの.envファイル作成
create_webapi_env:
	@if [ ! -f ./app/webapi/.env.example ]; then \
		echo "PYTHON_ENV=local" > ./app/webview/.env.example; \
	fi
	@if [ ! -f ./app/webapi/.env.local ]; then \
		cp -f ./app/webapi/.env.example ./app/webapi/.env.local; \
	fi
	@if [ ! -f ./app/webapi/.env.test ]; then \
		cp -f ./app/webapi/.env.example ./app/webapi/.env.test; \
	fi


# rdbのdataディレクトリ作成
create_rdb_data:
	@if [ ! -d ./app/rdb/postgresql/local ]; then \
		mkdir -p ./app/rdb/postgresql/local; \
	fi
	@if [ ! -d ./app/rdb/postgresql/test ]; then \
		mkdir -p ./app/rdb/postgresql/test; \
	fi

# kvsのdataディレクトリ作成
create_kvs_data:
	@if [ ! -d ./app/kvs/redis/local ]; then \
		mkdir -p ./app/kvs/redis/local; \
	fi
	@if [ ! -d ./app/kvs/redis/test ]; then \
		mkdir -p ./app/kvs/redis/test; \
	fi

# vectorのdataディレクトリ作成
create_vector_data:
	@if [ ! -d ./app/vector/qdrant/local ]; then \
		mkdir -p ./app/vector/qdrant/local; \
	fi
	@if [ ! -d ./app/vector/qdrant/test ]; then \
		mkdir -p ./app/vector/qdrant/test; \
	fi

# graphのdataディレクトリ作成
create_graph_data:
	@if [ ! -d ./app/graph/neo4j/local ]; then \
		mkdir -p ./app/graph/neo4j/local; \
	fi
	@if [ ! -d ./app/graph/neo4j/test ]; then \
		mkdir -p ./app/graph/neo4j/test; \
	fi

# 初期セットアップコマンド
init: create_root_env create_webapi_env create_webview_env create_rdb_data create_kvs_data create_vector_data create_graph_data

# Dockerコンテナ起動
docker-up:
	docker compose -f compose.${ENV}.yml up -d --build

# Dockerコンテナ削除
docker-down:
	docker compose -f compose.${ENV}.yml down --rmi all

# Docker解放
docker-free:
	docker system prune
