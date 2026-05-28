MODE ?= production

up:
	docker compose up -d --build

start:
	docker compose exec -d api sh -c "uv run base_code --mode $(MODE)" || (docker compose down && exit 1)

down:
	docker compose down

test:
	docker compose exec api uv run test || (docker compose down && exit 1)

coverage:
	@docker compose exec api sh -c "uv run pytest --cov=gc_api --cov-report=term 2>/dev/null | grep '^TOTAL' | awk '{print \$$NF}'"
