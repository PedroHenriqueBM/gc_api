import argparse

import uvicorn
from fastapi import FastAPI

from gc_api.fahrenheit_to_celsius import fahrenheit_to_celsius
from gc_api.celsius_to_fahrenheit import celsius_to_fahrenheit
from gc_api.settings import Settings

app = FastAPI()


@app.get("/convert/fahrenheit-to-celsius")
def convert_fahrenheit_to_celsius(value: float):
    result = fahrenheit_to_celsius(value)
    return {"fahrenheit": value, "celsius": round(result, 2)}


@app.get("/convert/celsius-to-fahrenheit")
def convert_celsius_to_fahrenheit(value: float):
    result = celsius_to_fahrenheit(value)
    return {"celsius": value, "fahrenheit": round(result, 2)}


def main():

    raise Exception("stop")

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="development", choices=["development", "production"])
    args = parser.parse_args()

    settings = Settings(_env_file=f".env.{args.mode}")
    print(f"[gc_api] mode: {args.mode}")
    uvicorn.run("gc_api.main:app", host=settings.host, port=settings.port, reload=settings.reload)
