from pydantic import BaseModel
from datetime import datetime

class UserStats(BaseModel):
    username: str
    user_id: int
    stat_type: str
    count: int
    date_value: datetime