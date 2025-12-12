# -------------------------------
# Start script for Rental-System
# -------------------------------

# Start backend
Write-Output "Starting backend..."
cd server
Start-Process "powershell" -ArgumentList ".\run_server.bat"

# Start frontend
Write-Output "Starting frontend..."
cd ..\client
Start-Process "powershell" -ArgumentList "npm run dev"

cd ..
Write-Output "Both backend and frontend started!"
