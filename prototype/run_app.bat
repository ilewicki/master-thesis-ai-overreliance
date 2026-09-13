@echo off
TITLE Launching Streamlit App

:: 1. Configuration - Base Miniconda path vs Environment path
SET CONDA_BASE=C:\Users\Igor\miniconda3
SET ENV_NAME=igor-thesis-poc
SET APP_PATH=E:\Magisterka\prototype\src\app.py

:: 2. Initialize Conda using the BASE installation path
CALL "%CONDA_BASE%\Scripts\activate.bat" "%CONDA_BASE%"

:: 3. Activate your target environment
echo Activating environment: %ENV_NAME%...
CALL conda activate %ENV_NAME%

:: 4. Navigate to your project directory
cd /d "E:\Magisterka\prototype\src"

:: 5. Launch the Streamlit application
echo Launching Streamlit...
streamlit run "%APP_PATH%"

pause