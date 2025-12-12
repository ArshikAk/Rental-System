from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db
from datetime import datetime

router = APIRouter(prefix="/cars", tags=["cars"])

@router.post("/", response_model=schemas.CarResponse, status_code=status.HTTP_201_CREATED)
def create_car(car_in: schemas.CarCreate, db: Session = Depends(get_db)):
    car = models.Car(
        make=car_in.make,
        model=car_in.model,
        year=car_in.year,
        daily_rate=car_in.daily_rate,
        available=True
    )
    db.add(car)
    db.commit()
    db.refresh(car)
    return car

@router.get("/", response_model=List[schemas.CarResponse])
def list_cars(db: Session = Depends(get_db)):
    return db.query(models.Car).all()

@router.get("/{car_id}", response_model=schemas.CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")
    return car
