@echo off
set DOWNLOAD_URL="https://github.com/arturbosch/detekt/releases/download/RC10/detekt-cli-1.0.0-RC10-all.jar"
set CACHE_DIR=%~dp0

echo %CACHE_DIR%

IF NOT EXIST "%CACHE_DIR%detekt.jar" (
    bitsadmin /transfer mydownload /dynamic /download /priority FOREGROUND "%DOWNLOAD_URL%" "%CACHE_DIR%\\detekt.jar"
)

set INPUT_FILES=""
set EXTRA_ARGS=""

setlocal enabledelayedexpansion
set ARGS=%*
for %%a in (%ARGS%) do ( 
   IF EXIST %%a (
       echo last: !INPUT_FILES!
       set INPUT_FILES=!INPUT_FILES!,%%a
   ) ELSE (
       set EXTRA_ARGS=!EXTRA_ARGS! %%a
   )
)
echo extras: %EXTRA_ARGS:~3%
echo input files: %INPUT_FILES:~3%

java -jar "%CACHE_DIR%detekt.jar" %EXTRA_ARGS:~3% -i %INPUT_FILES:~3%
endlocal
