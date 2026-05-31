from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int 

user = User(
    id = "101",
    name = "Kaku",
    age = 19
)

print(user)
