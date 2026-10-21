@echo off
cd /d "%~dp0"
if not exist node_modules\ (call npm.cmd ci || exit /b 1)
if not exist dist\index.html (call npm.cmd run build || exit /b 1)
echo Open http://127.0.0.1:4173/ in your browser. Keep this window open while serving.
call npm.cmd run preview -- --port 4173 --strictPort
