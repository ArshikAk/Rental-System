from fastapi import FastAPI
from app.database import Base, engine
from app.routers import cars, rentals

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Rental System API")

@app.get("/")
def home():
    return {"message": "Car Rental API is running!"}

# Include Routers
app.include_router(cars.router)
app.include_router(rentals.router)
