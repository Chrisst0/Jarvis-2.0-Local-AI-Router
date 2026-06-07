# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This workspace contains two PowerShell launcher scripts that configure and start Claude Code in either cloud or local mode.

## Launching

Run from a PowerShell terminal:

```powershell
# Cloud mode (Anthropic API, claude-4.6-sonnet)
.\jarvis-cloud.ps1

# Local mode (Ollama on localhost:11434, qwen3:4b)
.\jarvis-locale.ps1
```

## Architecture

Each script sets environment variables before invoking `claude`:

| Variable | Cloud | Local |
|---|---|---|
| `ANTHROPIC_API_KEY` | real API key | `"ollama"` (placeholder) |
| `ANTHROPIC_BASE_URL` | unset (default Anthropic) | `http://localhost:11434` |
| `ANTHROPIC_MODEL` | `claude-4.6-sonnet` | `qwen3:4b` |

The local mode relies on Ollama running at `localhost:11434` with the `qwen3:4b` model pulled.

## Switching Models

- To use Opus in cloud mode, change `$env:ANTHROPIC_MODEL` in `jarvis-cloud.ps1` to `claude-opus-4-6`
- To use a different Ollama model, change the value in `jarvis-locale.ps1` and ensure the model is pulled (`ollama pull <model>`)
