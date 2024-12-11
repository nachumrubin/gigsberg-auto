@echo off
:: Name of the virtual environment folder
set VENV_DIR=venv

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not added to PATH.
    exit /b 1
)

:: Check if the virtual environment folder already exists
if exist %VENV_DIR% (
    echo Virtual environment already exists in "%VENV_DIR%".
    exit /b 0
)

:: Create the virtual environment
python -m venv %VENV_DIR%
if %errorlevel% neq 0 (
    echo Failed to create the virtual environment.
    exit /b 1
)

echo Virtual environment created in "%VENV_DIR%".

:: Activate the virtual environment
call %VENV_DIR%\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate the virtual environment.
    exit /b 1
)

echo Virtual environment activated. You can now install dependencies.
pause
