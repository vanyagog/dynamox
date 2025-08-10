# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import List
from datetime import timedelta
from auth import create_access_token, decode_token
from users import get_user, verify_password

app = FastAPI(title="Backend with JWT Auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return None
    if not verify_password(password, user["password_hash"]):
        return None
    return {"username": username, "scopes": user.get("scopes", [])}

def get_current_user(token: str = Depends(oauth2_scheme)):
    from jwt import ExpiredSignatureError, InvalidTokenError
    try:
        payload = decode_token(token)
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return {"username": username, "scopes": payload.get("scopes", [])}

def require_scope(required_scope: str):
    def dependency(current_user = Depends(get_current_user)):
        scopes = current_user.get("scopes", [])
        if required_scope not in scopes:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return current_user
    return dependency

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    # Создаём токен на 60 минут
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(subject=user["username"], scopes=user["scopes"], expires_delta=access_token_expires)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/")
async def public_root():
    return {"message": "OK"}

@app.get("/count")
async def get_count(current_user = Depends(require_scope("read"))):
    # Здесь вернули бы настоящий счётчик — для примера возвращаем фиктивное число
    return {"successful_requests": 123, "requested_by": current_user["username"]}

@app.get("/admin")
async def admin_only(current_user = Depends(require_scope("write"))):
    return {"message": f"Hello admin {current_user['username']}"}
