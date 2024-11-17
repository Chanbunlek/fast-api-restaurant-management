from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    keycloak_server_url: str = Field(..., env="KEYCLOAK_SERVER_URL")
    keycloak_realm: str = Field(..., env="KEYCLOAK_REALM")
    keycloak_client_id: str = Field(..., env="KEYCLOAK_CLIENT_ID")
    keycloak_username: str = Field(..., env="KEYCLOAK_USERNAME")
    keycloak_password: str = Field(..., env="KEYCLOAK_PASSWORD")
    keycloak_client_secret: str = Field(..., env="KEYCLOAK_CLIENT_SECRET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()