# Genera AdoptaAPI_Informe_Profesional.pdf desde el HTML
$dir  = Split-Path -Parent $MyInvocation.MyCommand.Path
$html = Join-Path $dir "AdoptaAPI_Informe_Profesional.html"
$pdf  = Join-Path $dir "AdoptaAPI_Informe_Profesional.pdf"

if (-not (Test-Path $html)) {
    Write-Error "No se encontró: $html"
    exit 1
}

$edgePaths = @(
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe"
)

$browser = $edgePaths | Where-Object { Test-Path $_ } | Select-Object -First 1

if ($browser) {
    $uri = "file:///" + ($html -replace '\\', '/')
    & $browser --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$pdf" $uri
    Start-Sleep -Seconds 3
    if (Test-Path $pdf) {
        Write-Host "PDF generado exitosamente:" -ForegroundColor Green
        Write-Host $pdf
        Start-Process $pdf
        exit 0
    }
}

Write-Host "No se pudo generar PDF automaticamente." -ForegroundColor Yellow
Write-Host "Abre el HTML en el navegador y usa Ctrl+P -> Guardar como PDF"
Start-Process $html
