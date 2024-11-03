@echo off
setlocal

cd /d %~dp0

cd ../react_web_page/
start npm start

cd ..
start uvicorn fastapi_server.main:app --reload --port 8080
