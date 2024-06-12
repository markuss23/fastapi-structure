from typing import Any

from pydantic import (
    SecretStr,
    HttpUrl,
    AnyHttpUrl,
    IPvAnyAddress,
    field_validator,
    Field,
    BaseModel,
    model_validator,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


from typing import Annotated


Port = Annotated[int, Field(ge=0, le=65535)]


def normalize_none(env_value: str) -> Any | None:
    if env_value == "":
        return None
    return env_value


class AppSettings(BaseModel):
    name: str | None
    timezone: str | None
    host: str | None
    port: int | None
    debug: bool = True
    root_path: str | None

    @model_validator(mode="before")
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


class SqlSettings(BaseModel):
    host: str
    port: Port
    user: str
    password: SecretStr
    database: str

    normalize_none = field_validator("*", mode="before")(normalize_none)

    def url(self) -> str:
        return f"mysql+pymysql://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):

    app: AppSettings
    sql: SqlSettings | None = None

    model_config = SettingsConfigDict(
        env_file=".env",  # Pokud není definováno, nenačte se žádný soubor.
        env_file_encoding="utf-8",  # Pokud není definováno, použije se kódování systému
        case_sensitive=False,  # Pokud není definováno, použije se hodnota False
        extra="ignore",  # Pokud není definováno, použije se hodnota "forbid"
        arbitrary_types_allowed=True,  # Pokud není definováno, použije se hodnota False
        env_nested_delimiter="__",  # Definice víceúrovňových proměnných
    )


settings = Settings()
