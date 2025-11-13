@echo off
REM Requer gcc (MinGW) ou cl (MSVC) no PATH.
gcc -shared -o c_module.dll c_module.c
echo Gerado: c_module.dll
