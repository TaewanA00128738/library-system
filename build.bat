@echo off

REM Define variables
set ENV_DIR=myenv
set SCRIPT=library_system.py
set DIST_DIR=dist
set EXECUTABLE=library_system.exe

REM Create a virtual environment
echo Creating virtual environment...
python -m venv %ENV_DIR%

REM Activate the virtual environment
call %ENV_DIR%\Scripts\activate

REM Install required packages
echo Installing required packages...
pip install pyinstaller

REM Run tests
echo Running tests...
python -m unittest test-library-system.py
if %ERRORLEVEL% NEQ 0 (
    echo Tests failed. Exiting.
    call %ENV_DIR%\Scripts\deactivate
    exit /b 1
)

REM Create the executable
echo Creating executable...
pyinstaller --onefile %SCRIPT%

REM Check if the executable was created successfully
if exist "%DIST_DIR%\%EXECUTABLE%" (
    echo Executable created successfully.
) else (
    echo Failed to create executable. Exiting.
    call %ENV_DIR%\Scripts\deactivate
    exit /b 1
)

REM Deactivate the virtual environment
call %ENV_DIR%\Scripts\deactivate

echo Build process completed successfully.