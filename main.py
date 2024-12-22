from fastapi import FastAPI
from db import schemas

users = [schemas.User(id=0, username="Globus", email = "globus.gr@gmail.com"),
         schemas.User(id=1, username="Globus2", email = "globus.gr2@gmail.com")]
app = FastAPI()

@app.post("/create-user/")
def create_user(user: schemas.User):
    users.append(user)
    print(users)
@app.get("/users/")
def get_users():
    return users
@app.get("/users/{user_id}/")
def get_users(users_id: int):
    result = []
    for user in users:
        if user.id == users_id:
            return user
        

if __name__ == "__main__":
    import os

    os.system("uvicorn main:app --reload")