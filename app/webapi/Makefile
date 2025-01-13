.PHONY: migration migrate test test-unit test-integration test-e2e

# make migration file (ex: make migration MESSAGE="init")
migration:
	docker exec -it -w /webapi webapi alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	docker exec -it -w /webapi webapi alembic upgrade head

test:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests

test-unit:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests/unit

test-integration:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests/integration

test-e2e:
	docker exec -it -w /webapi webapi pytest --cov --cov-branch -vs tests/e2e
