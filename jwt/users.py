# users.py
from passlib.context import CryptContext
from typing import Dict

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Пример: храним пользователей в памяти {username: {password_hash, scopes}}
fake_users_db: Dict[str, dict] = {
    "alice": {
        "password_hash": pwd_context.hash("alicepassword"),
        "scopes": ["read"]
    },
    "bob": {
        "password_hash": pwd_context.hash("bobpassword"),
        "scopes": ["read", "write"]
    }
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    return fake_users_db.get(username)
