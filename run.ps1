Start-Process -FilePath "python" -ArgumentList "stackreg.py" -NoNewWindow -Wait
Write-Host "Press any key to exit..."
Read-Host