# -------------------------------
# Setup script for Rental-System
# -------------------------------

# 1. Setup Python virtual environment in server
Write-Output "Creating Python virtual environment..."
cd server
python -m venv venv

Write-Output "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# 2. Upgrade pip and install Python dependencies
Write-Output "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 3. Initialize the database
Write-Output "Initializing database..."
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
Write-Output "Database initialized"

# 4. Setup frontend
Write-Output "Installing frontend dependencies..."
cd ..\client
npm install
Write-Output "Frontend dependencies installed"

cd ..
Write-Output "Setup completed successfully!"
