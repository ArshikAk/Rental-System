from fastapi import FastAPI

app = FastAPI(title="Car Rental System")

@app.get("/")
def home():
    return {"message": "Car Rental System API is running"}
