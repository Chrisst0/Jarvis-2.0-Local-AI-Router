# Jarvis cloud mode – Claude Code + Anthropic (Sonnet)

# 1) L'API key Anthropic deve essere già impostata come variabile d'ambiente:
#    - Variabile utente di Windows: ANTHROPIC_API_KEY=sk-ant-...
#    - Oppure impostata prima di lanciare questo script

# 2) Assicurati di NON usare l'endpoint locale di Ollama
Remove-Item Env:ANTHROPIC_BASE_URL -ErrorAction SilentlyContinue
Remove-Item Env:ANTHROPIC_MODEL -ErrorAction SilentlyContinue

# 3) (Opzionale) Forza il modello se vuoi, altrimenti lascia che /model scelga
# $Env:ANTHROPIC_MODEL = "sonnet-4.6"   # usa il nome esatto che ti dà /model, oppure commenta questa riga

# 4) Vai nella cartella del progetto Jarvis
Set-Location "F:\Projects\Jarvis"

# 5) Avvia Claude Code nel progetto
claude
