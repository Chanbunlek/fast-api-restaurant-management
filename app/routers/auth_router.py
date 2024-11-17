from fastapi import HTTPException, Form, APIRouter
from models.auth import TokenResponse
from controller.auth import AuthController
from config.keycloak import keycloak_admin
from schemas.user import User

auth = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

@auth.get("/")
async def read_root():
    return AuthController.read_root()

@auth.post("/login", response_model=TokenResponse)
async def login(username: str = Form(...), password: str = Form(...)):
    return AuthController.login(username, password)

@auth.post("/create_user")
async def create_user(user: User):
    try:
        new_user = keycloak_admin.create_user({
            "username": user.username,
            "email": user.email,
            "firstName": user.first_name,
            "lastName": user.last_name,
            "enabled": True,
            "credentials": [{
                "type": "password",
                "value": user.password,
                "temporary": False
            }]
        })

        return {"message": "User created successfully", "user_id": new_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
