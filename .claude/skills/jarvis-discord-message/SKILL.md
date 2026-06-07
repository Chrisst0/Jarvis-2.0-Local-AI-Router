---
name: jarvis-discord-message
description: Manda un messaggio su Discord tramite lo script locale Jarvis (main.py) usando un file JSON di task.
author: chris
version: 0.1.0
# Per ora lascia che sia solo l'utente a invocarla esplicitamente con /jarvis-discord-message
disable-model-invocation: false
---

# Skill `jarvis-discord-message`

Questa skill manda un messaggio su Discord usando lo script locale `main.py` nella repo Jarvis (`F:\Projects\Jarvis\`), tramite un file di task JSON.

## Quando usare questa skill

Usa questa skill quando:
- l'utente chiede esplicitamente di mandare un messaggio su Discord,
- vuoi usare il pipeline locale Jarvis (`main.py` + `send_ds_webhook.py`) invece di chiamare direttamente le API Discord.

## Parametri richiesti

Questa skill richiede un solo parametro:

- `message` (obbligatorio): testo completo del messaggio da inviare su Discord.

Quando l'utente invoca `/jarvis-discord-message` o chiede di usare questa skill, chiedi il valore di `message` se non è chiaro dal contesto.

## File e percorso

La repo locale è:

- `F:\Projects\Jarvis\`

Il file di task deve essere:

- `F:\Projects\Jarvis\tasks\current_task.json`

Se la cartella `tasks` non esiste, creala.

## Formato del file JSON

Il contenuto di `current_task.json` deve essere SEMPRE un JSON con questo schema:

```json
{
  "type": "discord.send_message",
  "payload": {
    "message": "<TESTO_DEL_MESSAGGIO>"
  }
}
