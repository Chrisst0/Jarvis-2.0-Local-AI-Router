param(
    [Parameter(Mandatory = $true)]
    [string]$Action
)

# Mappa delle azioni consentite -> comando da eseguire
$whitelist = @{
    "open_vscode" = "C:\Users\Chris\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    "open_chrome" = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    "open_obs"    = "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
}

if (-not $whitelist.ContainsKey($Action)) {
    Write-Output "DENY: action '$Action' is not allowed."
    exit 1
}

$target = $whitelist[$Action]

Start-Process -FilePath $target
Write-Output "OK: executed '$Action' -> $target"
exit 0
