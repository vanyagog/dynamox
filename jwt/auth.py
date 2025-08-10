# auth.py
import os
from datetime import datetime, timedelta
from typing import Optional, List
import jwt

# параметры токена — выносить в env vars
JWT_SECRET = os.getenv("JWT_SECRET", "change_me_in_prod")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

def create_access_token(subject: str, scopes: Optional[List[str]] = None, expires_delta: Optional[timedelta] = None) -> str:
    now = datetime.utcnow()
    if expires_delta:
        exp = now + expires_delta
    else:
        exp = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": subject,
        "scopes": scopes or [],
        "iat": now,
        "exp": exp
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    # pyjwt returns str in v2+
    return token

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise
    except jwt.InvalidTokenError:
        raise
