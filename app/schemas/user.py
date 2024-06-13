from pydantic import BaseModel

class User(BaseModel):
    name: str = None
    email: str = None
    password: str = None
