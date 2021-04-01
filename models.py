from pydantic import BaseModel, validator
import datetime

class Task(BaseModel):
    num: int
    time_sleep : float
    time_create: datetime.datetime
    @validator('time_sleep')
    def time_sleep_non_negative(cls,v):
        if v<0:
            raise ValueError('time_sleep<0')
        return v
    