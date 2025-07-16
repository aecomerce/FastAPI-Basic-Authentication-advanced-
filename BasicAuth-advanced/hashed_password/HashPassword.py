from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# hashed = pwd_context.hash("your_password")
# pwd_context.verify("your_password", hashed)
