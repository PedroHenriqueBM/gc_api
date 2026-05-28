MODE ?= production

up:
	docker compose up -d --build

start:
	docker compose exec -d api sh -c "uv run base_code --mode $(MODE)" || (docker compose down && exit 1)

down:
	docker compose down

test:
	docker compose exec api uv run test || (docker compose down && exit 1)
