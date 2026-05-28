# gc_api

API REST para conversão de temperaturas entre Celsius e Fahrenheit, construída com FastAPI.

## Pré-requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Instalação

```bash
uv venv               # cria o ambiente virtual (.venv)
uv sync               # dependências de produção
uv sync --extra dev   # inclui pytest para testes
```

## Configuração

O ambiente é definido via flag `--mode` ao iniciar a API. Cada modo carrega o arquivo `.env` correspondente:

| Modo | Arquivo carregado |
|------|-------------------|
| `development` (padrão) | `.env.development` |
| `production` | `.env.production` |

Variáveis disponíveis (ver `.env.example`):

| Variável | Descrição |
|----------|-----------|
| `HOST` | Endereço de escuta |
| `PORT` | Porta |
| `RELOAD` | Hot-reload (uvicorn) |

## Rodando a API

```bash
uv run base_code                       # modo development (padrão)
uv run base_code --mode=development
uv run base_code --mode=production
```

A API estará disponível em `http://localhost:8000`.  
Documentação interativa: `http://localhost:8000/docs`

## Docker

Requer [Docker](https://docs.docker.com/get-docker/) instalado.

O modo é controlado pela variável de ambiente `MODE` passada na execução. O padrão é `production`.

```bash
docker compose up -d --build                      # production (padrão)
MODE=development docker compose up -d --build     # development
MODE=production docker compose up -d --build      # production
```

## Testes

```bash
uv run test          # roda todos os testes
uv run test -v       # verbose
uv run test -k nome  # filtra por nome
```

> Requer `uv sync --extra dev` antes de rodar pela primeira vez.

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/convert/fahrenheit-to-celsius?value={n}` | Converte Fahrenheit para Celsius |
| GET | `/convert/celsius-to-fahrenheit?value={n}` | Converte Celsius para Fahrenheit |

```bash
curl "http://localhost:8000/convert/fahrenheit-to-celsius?value=100"
# {"fahrenheit": 100.0, "celsius": 37.78}

curl "http://localhost:8000/convert/celsius-to-fahrenheit?value=37"
# {"celsius": 37.0, "fahrenheit": 98.6}
```
