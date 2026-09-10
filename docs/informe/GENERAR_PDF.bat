@echo off
echo Generando PDF de AdoptaAPI...
powershell -ExecutionPolicy Bypass -File "%~dp0generar_pdf.ps1"
pause
