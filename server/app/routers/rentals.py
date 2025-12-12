from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from datetime import datetime
from typing import List

router = APIRouter(prefix="/rentals", tags=["rentals"])

def rentals_overlap_query(qs, car_id: int, start_dt: datetime, end_dt: datetime):
    """
    filters qs (query) to rentals that overlap given period for given car_id and active==True
    overlap condition: existing.start <= requested.end AND existing.end >= requested.start
    """
    return qs.filter(
        models.Rental.car_id == car_id,
        models.Rental.active == True,
        models.Rental.start_date <= end_dt,
        models.Rental.end_date >= start_dt
    )

def any_car_available_for_period(db: Session, start_dt: datetime, end_dt: datetime) -> bool:
    """
    Return True if at least one car has NO overlapping active rentals for the requested period.
    """
    cars = db.query(models.Car).all()
    for car in cars:
        overlaps = db.query(models.Rental).filter(
            models.Rental.car_id == car.id,
            models.Rental.active == True,
            models.Rental.start_date <= end_dt,
            models.Rental.end_date >= start_dt
        ).all()
        if not overlaps:
            return True
    return False

@router.post("/{car_id}/rent", response_model=schemas.RentalResponse, status_code=status.HTTP_201_CREATED)
def rent_car(car_id: int, rental_in: schemas.RentalCreate, db: Session = Depends(get_db)):
    
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")

   
    start_dt = rental_in.start_date
    end_dt = rental_in.end_date
    if end_dt < start_dt:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="end_date must be >= start_date")

    
    overlapping = rentals_overlap_query(db.query(models.Rental), car_id, start_dt, end_dt).all()
    if overlapping:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Car is already rented for the specified dates")

    
    if not any_car_available_for_period(db, start_dt, end_dt):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No cars are available for the specified dates")

    
    rental = models.Rental(
        car_id=car_id,
        user_name=rental_in.user_name,
        start_date=start_dt,
        end_date=end_dt,
        active=True
    )
    db.add(rental)
    db.commit()
    db.refresh(rental)
    return rental

@router.delete("/{rental_id}", status_code=status.HTTP_200_OK)
def cancel_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    if not rental or not rental.active:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Active rental not found")

    
    rental.active = False
    db.add(rental)
    db.commit()

    return {"detail": "rental canceled", "rental_id": rental_id}


@router.get("/", response_model=List[schemas.RentalResponse])
def list_rentals(db: Session = Depends(get_db)):
    return db.query(models.Rental).all()

@router.get("/active", response_model=List[schemas.RentalResponse])
def active_rentals(db: Session = Depends(get_db)):
    return db.query(models.Rental).filter(models.Rental.active == True).all()
