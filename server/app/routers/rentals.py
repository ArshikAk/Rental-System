from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/rentals", tags=["Rentals"])

@router.post("/{car_id}/rent", response_model=schemas.Rental)
def rent_car(car_id: int, rental: schemas.RentalCreate, db: Session = Depends(get_db)):

    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    # Check date overlap
    overlapping = db.query(models.Rental).filter(
        models.Rental.car_id == car_id,
        models.Rental.active == True,
        models.Rental.start_date <= rental.end_date,
        models.Rental.end_date >= rental.start_date
    ).all()

    if overlapping:
        raise HTTPException(status_code=400, detail="Car unavailable for selected dates")

    new_rental = models.Rental(
        car_id=car_id,
        user_name=rental.user_name,
        start_date=rental.start_date,
        end_date=rental.end_date,
        active=True
    )
    db.add(new_rental)
    db.commit()
    db.refresh(new_rental)
    return new_rental


@router.delete("/{rental_id}")
def cancel_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = db.query(models.Rental).filter(models.Rental.id == rental_id, models.Rental.active == True).first()

    if not rental:
        raise HTTPException(status_code=404, detail="Active rental not found")

    rental.active = False
    db.commit()
    return {"detail": "Rental canceled"}
