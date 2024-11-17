from fastapi import Depends, HTTPException, status, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.auth import TokenResponse, UserInfo
from service.auth import AuthService

bearer_scheme = HTTPBearer()

class AuthController:
    @staticmethod
    def read_root():
        return {
            "message": (
                "Welcome to the Keycloak authentication system. "
                "Use the /login endpoint to authenticate and /protected to access the protected resource."
            ),
            "documentation": "/docs",
        }

    @staticmethod
    def login(username: str = Form(...), password: str = Form(...)) -> TokenResponse:
        access_token = AuthService.authenticate_user(username, password)

        if not access_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        return TokenResponse(access_token=access_token)

    @staticmethod
    def protected_endpoint(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    ) -> UserInfo:
        token = credentials.credentials

        user_info = AuthService.verify_token(token)

        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return user_info