@echo off
echo Getting free disk space using PowerShell...

powershell -Command "Get-PSDrive -Name C | Select-Object @{Name='FreeSpace(GB)';Expression={[math]::round($_.Free/1GB, 2)}}"