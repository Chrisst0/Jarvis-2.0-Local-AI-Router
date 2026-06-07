[![License](https://img.shields.io/github/license/Chrisst0/Jarvis-2.0-Local-AI-Router.svg)](./LICENSE)
![Language](https://img.shields.io/github/languages/top/Chrisst0/Jarvis-2.0-Local-AI-Router.svg)
![Status](https://img.shields.io/badge/status-in_development-yellow)
![Version](https://img.shields.io/badge/version-0.1.0-blue)


# Jarvis 2.0 – Local AI router

Questo progetto nasce come capolavoro del triennio delle scuole superiori e ha l'obiettivo di creare un assistente personale che instrada in modo intelligente le richieste tra modelli di intelligenza artificiale locali e cloud, privilegiando i modelli locali per ridurre i costi.

Questo repository contiene una versione semplificata e ripulita del progetto, pensata per essere consultata come esempio didattico e come documentazione del capolavoro.

## Funzionalità principali

- Integrazione con Discord come canale principale di input.
- Router logico che decide se usare un modello locale o Claude (cloud) in base al tipo di richiesta.
- Monitoraggio dei costi delle sessioni cloud tramite Cost Guardian e SQLite.
- Status line personalizzata che mostra in tempo reale costo totale e token utilizzati.
- Integrazione di plugin per memoria persistente e controllo dei costi.

## Struttura del progetto (semplificata)

- `main.py`: punto di ingresso principale.
- `asklocal_bot.py`, `send_ds_message.py`, `send_ds_webhook.py`: script collegati al bot e a Discord.
- `agents/`: agenti specifici, ad esempio per il controllo di Windows.
- `scripts/windows/`: script PowerShell di supporto.
- `.claude/skills/`: definizioni delle skill utilizzate da Claude Code (versioni ripulite per questo repo).
- `tasks/` e file JSON di esempio: definizione dei task e configurazioni base.

## Nota

Per motivi di sicurezza, il repository **non** contiene chiavi, credenziali o file di configurazione completi. Alcuni file (`settings.local.json`, database, memorie locali) sono stati esclusi e vanno ricreati o adattati in base al proprio ambiente.

## Struttura del codice

La struttura reale del progetto in locale è simile alla seguente (alcuni file, come impostazioni locali e database, sono esclusi dal repository pubblico):

```
Jarvis
├─ .claude
│  └─ skills
│     ├─ jarvis-discord-message
│     │  └─ SKILL.md
│     └─ local-code-qwen
│        └─ SKILL.md
├─ agents
│  └─ windows_control_agent.py
├─ asklocal_bot.py
├─ CLAUDE.md
├─ jarvis-cloud.ps1
├─ jarvis-locale.ps1
├─ main.py
├─ scripts
│  └─ windows
│     └─ run_whitelisted.ps1
├─ send_ds_message.py
├─ send_ds_webhook.py
├─ tasks
│  └─ current_task.json (o un esempio)
└─ task_ds.json
```
Cartelle come .swarm/ e file di configurazione locali (ad esempio settings.local.json, database e memorie) non sono presenti nel repository pubblico per motivi di sicurezza e privacy.