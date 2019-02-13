@echo off

setlocal enabledelayedexpansion
set /a count=0
for %%a in (%*) do (
    set /a count+=1
    echo %%a : !count!
)
endlocal