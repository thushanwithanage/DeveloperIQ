from pydantic import BaseModel
import json

class User(BaseModel):
    username: str
    user_id: int