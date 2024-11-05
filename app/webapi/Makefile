.PHONY: migration migrate

# make migration file (ex: make migration MESSAGE="init")
migration:
	docker exec -it -w /webapi webapi alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	docker exec -it -w /webapi webapi alembic upgrade head




