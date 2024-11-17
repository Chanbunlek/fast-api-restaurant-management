from fastapi import FastAPI, Depends
from routers.auth_router import auth
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models.auth import UserInfo
from controller.auth import AuthController

app = FastAPI()
bearer_scheme = HTTPBearer()
app.include_router(auth)

@app.get("/protected", response_model=UserInfo)
async def protected_endpoint(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    return AuthController.protected_endpoint(credentials)