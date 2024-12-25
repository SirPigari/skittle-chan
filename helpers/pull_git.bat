@echo off
REM Change directory to the location of the script
cd /d "%~dp0" >nul

REM Navigate to the parent directory (assumes this is where the Git repo is)
cd .. >nul

REM Switch to the main branch
git checkout main

REM Commit changes with a message
git commit -m "Save local changes"

REM Pull the latest changes from the remote repository
git pull

pause