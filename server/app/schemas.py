from pydantic import BaseModel
from datetime import datetime

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    daily_rate: float


class CarResponse(BaseModel):
    id: int
    make: str
    model: str
    year: int
    daily_rate: float
    available: bool

    class Config:
        orm_mode = True


class RentalCreate(BaseModel):
    user_name: str
    start_date: datetime
    end_date: datetime


class RentalResponse(BaseModel):
    id: int
    car_id: int
    user_name: str
    start_date: datetime
    end_date: datetime
    active: bool

    class Config:
        orm_mode = True
