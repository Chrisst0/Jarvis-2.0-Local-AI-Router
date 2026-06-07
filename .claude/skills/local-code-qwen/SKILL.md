---
name: local-code-qwen
description: Usa il modello locale Qwen3:4b via Ollama per generare o modificare codice, evitando l'uso di modelli cloud quando possibile.
author: chris
version: 0.1.0
---

# Skill `local-code-qwen`

Questa skill serve per usare il modello locale `qwen3:4b` tramite `ollama run qwen3:4b` per tutti i task di coding dove è sufficiente un modello locale.

## Quando usare questa skill

Usa questa skill quando:
- l'utente chiede di scrivere, completare o refactorare codice;
- l'utente chiede snippet, funzioni, piccoli script;
- l'utente non ha esplicitamente chiesto di usare Claude cloud / Sonnet / Opus.

Non usare questa skill quando:
- l'utente chiede analisi architetturali complesse;
- l'utente chiede esplicitamente di usare un modello cloud;
- serve un contesto molto grande o reasoning profondo.

## Parametri

Questa skill richiede un parametro principale:

- `prompt` (obbligatorio): istruzioni da passare al modello Qwen3:4b per generare o modificare codice.

Il prompt deve includere:
- il contesto minimo necessario (es. estratto di codice, linguaggio, obiettivo),
- richieste chiare su stile e formato dell'output.

## Procedura operativa

Quando usi questa skill:

1. Costruisci una stringa di prompt per Qwen3:4b che includa:
   - una breve istruzione su cosa deve fare (in inglese o italiano chiaro),
   - eventuali snippet di codice rilevanti,
   - il formato atteso dell'output (ad esempio: "rispondi solo con il codice, senza spiegazioni").

2. Esegui il comando da terminale nella macchina locale:

   ```bash
   ollama run qwen3:4b
