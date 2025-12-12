from fastapi import FastAPI
from app.routers import cars, rentals
from app.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental API")

app.include_router(cars.router)
app.include_router(rentals.router)

@app.get("/")
def root():
    return {"message": "Car Rental API is running"}
