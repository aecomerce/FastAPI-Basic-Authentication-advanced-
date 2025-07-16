# 🚀 FastAPI Basic Authentication (advanced)

Secure authentication using password hashing and protection against timing attacks has been implemented. 

## 🔹 Implemented  

- **Creating data models** (UserBase, User(UserBase), UserlnDB(UserBase))  
- **Basic HTTP Auth** (username/password validation)  
- **Setting up PassLib** (CryptContext[Bcrypt])
- **Authentication dependency**
- **Implementation of the /register and /login routes**
- **Error handling (optional)**

## 🔹 Technologies Used

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **CryptContext**

## 🔹 Testing via curl

# Registration
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"correctpass"}' http://localhost:8000/register

# Successful login
curl -u user1:correctpass http://localhost:8000/login

# Wrong password
curl -u user1:wrongpass http://localhost:8000/login
