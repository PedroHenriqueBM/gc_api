from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    reload: bool
