@echo off
echo Checking if the file exists to move...

:: Set the source and destination directories
set SOURCE_FILE=C:\temp\que1.txt
set DEST_DIR=C:\temp\newfolddest
set DEST_FILE=%DEST_DIR%\que1.txt

:: Check if the file exists at the source location
if not exist "%SOURCE_FILE%" (
    echo Source file does not exist. Exiting...
    exit /b 0
)

:: Check if the destination folder exists, if not, create it
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

:: Delete the file at the destination if it exists
if exist "%DEST_FILE%" (
    echo File exists at the destination. Replacing it...
    del "%DEST_FILE%"
)

:: Move the text file to the new directory
move "%SOURCE_FILE%" "%DEST_FILE%"

:: Check if the move was successful
if exist "%DEST_FILE%" (
    echo File moved and replaced successfully!
) else (
    echo Failed to move the file.
)

exit /b 0
