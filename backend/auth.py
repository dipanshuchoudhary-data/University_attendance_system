from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = "qazwsxedc123"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password,hased):
    return pwd_context.verify(password,hased)

def create_token(data:dict):
    return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)