@echo off
setlocal

cd /d %~dp0

cd ../react_web_page/
start npm start

cd ../fastapi_server/scripts/
start run.bat
