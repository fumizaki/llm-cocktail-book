.PHONY: migration migrate test

# make migration file (ex: make migration MESSAGE="init")
migration:
	docker exec -it -w /webapi webapi alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	docker exec -it -w /webapi webapi alembic upgrade head

test:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests


