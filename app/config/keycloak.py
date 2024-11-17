from config.setting import settings
from keycloak import KeycloakOpenID, KeycloakOpenIDConnection, KeycloakAdmin

keycloak_openid = KeycloakOpenID(
    server_url=settings.keycloak_server_url,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    client_secret_key=settings.keycloak_client_secret,
)

keycloak_connection = KeycloakOpenIDConnection(
    server_url=settings.keycloak_server_url,
    username=settings.keycloak_username,
    password=settings.keycloak_password,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    verify=True
)

keycloak_admin = KeycloakAdmin(
    server_url=settings.keycloak_server_url,
    username=settings.keycloak_username,
    password=settings.keycloak_password,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    client_secret_key=settings.keycloak_client_secret,
    verify=True
)

def get_openid_config():
    return keycloak_openid.well_known()