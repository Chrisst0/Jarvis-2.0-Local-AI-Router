# Jarvis local mode – Claude Code + Ollama (no Anthropic cost)

# Configura env per usare SOLO Ollama locale
$env:ANTHROPIC_API_KEY = "ollama"
$env:ANTHROPIC_BASE_URL = "http://localhost:11434"
$env:ANTHROPIC_MODEL = "qwen3:4b"

# (opzionale) disattiva eventuali chiavi Anthropic residue
Remove-Item Env:ANTHROPIC_REAL_API_KEY -ErrorAction SilentlyContinue

# Vai nella cartella del progetto Jarvis (modifica se serve)
Set-Location "F:\Projects\Jarvis"

# Avvia Claude Code nel progetto
claude

function Invoke-JarvisApp {
    param(
        [Parameter(Mandatory = $true)]
        [ValidateSet("vscode", "chrome", "obs")]
        [string]$App
    )

    $actionMap = @{
        "vscode" = "open_vscode"
        "chrome" = "open_chrome"
        "obs"    = "open_obs"
    }

    $action = $actionMap[$App]

    powershell -ExecutionPolicy Bypass -File `
        "F:\Projects\Jarvis\scripts\windows\run_whitelisted.ps1" `
        -Action $action
}

function Invoke-JarvisDiscord {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    python "F:\Projects\Jarvis\send_ds_webhook.py" $Message
}
