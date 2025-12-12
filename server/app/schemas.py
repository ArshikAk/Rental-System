from pydantic import BaseModel
from datetime import datetime

class CarBase(BaseModel):
    make: str
    model: str
    year: int
    daily_rate: float

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    available: bool

    class Config:
        orm_mode = True


class RentalBase(BaseModel):
    user_name: str
    start_date: datetime
    end_date: datetime

class RentalCreate(RentalBase):
    pass

class Rental(RentalBase):
    id: int
    car_id: int
    active: bool

    class Config:
        orm_mode = True
