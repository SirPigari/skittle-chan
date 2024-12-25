@echo off
REM Change Directory to the location of the script
cd /d "%~dp0" >nul

REM Move one directory up
cd .. >nul

REM Ensure you're on the 'main' branch
git checkout main

REM Remove all files from Git's index (not from local)
git rm -r --cached .

REM Commit the removal
git commit -m "Remove all files from the repository"

REM Push the removal to GitHub
git push origin main

REM Re-add all the files you want to push
git add .

REM Commit the re-added files
git commit -m "Re-add project files"

REM Push the re-added files to GitHub
git push origin main

REM Pause the script to see output
pause
