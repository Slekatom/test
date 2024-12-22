from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

    def __repr__(self):
        return f"{self.id} - {self.username}"