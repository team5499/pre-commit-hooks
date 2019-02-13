@echo off

set DOWNLOAD_URL="https://github.com/shyiko/ktlint/releases/download/0.29.0/ktlint"
set CACHE_DIR=%~dp0

echo %CACHE_DIR%

IF NOT EXIST "%CACHE_DIR%ktlint" (
    bitsadmin /transfer mydownload /dynamic /download /priority FOREGROUND "%DOWNLOAD_URL%" "%CACHE_DIR%\\ktlint"
)

setlocal enabledelayedexpansion
set ARGS=%*

"C:\Program Files\Git\bin\sh.exe" "%CACHE_DIR%ktlint" %ARGS%
endlocal
