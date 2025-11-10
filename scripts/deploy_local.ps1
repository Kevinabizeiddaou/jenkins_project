$ErrorActionPreference = "Stop"
$deployDir = "$env:WORKSPACE\deploy"
if (!(Test-Path $deployDir)) {
  New-Item -ItemType Directory -Path $deployDir | Out-Null
}
Copy-Item -Path "$env:WORKSPACE\dist\*" -Destination $deployDir -Recurse -Force
Write-Host "Deployed to $deployDir"
