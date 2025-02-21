.PHONY: migration migrate test

# デフォルトのPATHを / に設定
PATH ?= /

# make migration file (ex: make migration MESSAGE="init")
migration:
	docker exec -it -w /webapi webapi alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	docker exec -it -w /webapi webapi alembic upgrade head

# run test (ex: make test PATH="/unit")
test:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests${PATH}
