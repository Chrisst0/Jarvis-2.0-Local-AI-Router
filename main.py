# Jarvis main entrypoint
import json
import subprocess
import sys
from typing import Any, Dict


def handle_windows_action(payload: Dict[str, Any]) -> str:
    action = payload.get("action")
    if not action:
        return "Missing 'action' in payload."

    cmd = [
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-File",
        r"F:\Projects\Jarvis\scripts\windows\run_whitelisted.ps1",
        "-Action",
        action,
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=15,
    )

    if result.returncode != 0:
        return f"PowerShell error (code {result.returncode}): {(result.stdout or result.stderr).strip()}"

    return (result.stdout or "").strip() or "OK"


def handle_discord_message(payload: Dict[str, Any]) -> str:
    message = payload.get("message")
    if not message:
        return "Missing 'message' in payload."

    cmd = [
        "python",
        r"F:\Projects\Jarvis\send_ds_webhook.py",
        message,
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=15,
    )

    if result.returncode != 0:
        return f"Discord webhook error (code {result.returncode}): {(result.stdout or result.stderr).strip()}"

    return (result.stdout or "").strip() or "OK"


def handle_ai_chat(payload: Dict[str, Any]) -> str:
    import re

    user_prompt = payload.get("prompt")
    if not user_prompt:
        return "Missing 'prompt' in payload."

    # Capisci se l'utente parla di "bullet points / ideas / points / tips"
    wants_bullets = bool(
        re.search(r"\b(bullet|bullets|points?|ideas?|tips?)\b", user_prompt, re.IGNORECASE)
    )

    n = 3  # default
    if wants_bullets:
        m = re.search(r"\b(\d+)\b", user_prompt)
        if m:
            n = int(m.group(1))
            if n <= 0 or n > 10:
                n = 3

    if wants_bullets:
        system_prompt = (
            "You are Jarvis, a concise technical assistant.\n"
            "RULES:\n"
            f"- Output EXACTLY {n} bullet points.\n"
            "- Always respond in English.\n"
            "- Each bullet is one short sentence (max 15 words).\n"
            "- Little to NO explanation of your reasoning.\n"
            "- NO preface, NO thinking, NO meta-comments.\n"
            "- Start directly with the bullet points.\n"
        )
    else:
        system_prompt = (
            "You are Jarvis, a concise technical assistant.\n"
            "RULES:\n"
            "- Always respond in English.\n"
            "- Provide a direct answer in 1–3 short sentences.\n"
            "- NO preface, NO thinking, NO meta-comments.\n"
            "- Do NOT use bullet points unless explicitly requested.\n"
        )

    full_prompt = f"{system_prompt}\nUser request:\n{user_prompt}\n\nAnswer:\n"

    cmd = ["ollama", "run", "qwen3:4b-instruct"]

    try:
        result = subprocess.run(
            cmd,
            input=full_prompt,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        return "Error: 'ollama' command not found. Is Ollama installed and in PATH?"

    if result.returncode != 0:
        return f"Ollama error (code {result.returncode}): {(result.stdout or result.stderr).strip()}"

    text = (result.stdout or "").strip()
    if not text:
        return "No response from model."

    return text

def handle_task(task: Dict[str, Any]) -> str:
    ttype = task.get("type")
    payload = task.get("payload") or {}

    if ttype == "windows.action":
        return handle_windows_action(payload)
    elif ttype == "discord.send_message":
        return handle_discord_message(payload)
    elif ttype == "ai.chat":
        return handle_ai_chat(payload)
    else:
        return f"Unknown task type: {ttype}"


def main_interactive() -> None:
    print("Jarvis main – enter task JSON, empty line to quit.")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break

        if not line:
            break

        try:
            task = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            continue

        result = handle_task(task)
        print(f"RESULT: {result}")


def main() -> None:
    # Usage:
    #   python main.py
    #   python main.py --task "<json>"
    #   python main.py --task-file task_ds.json
    if len(sys.argv) >= 3 and sys.argv[1] == "--task":
        raw = sys.argv[2]
        try:
            task = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in --task: {e}")
            sys.exit(1)

        result = handle_task(task)
        print(f"RESULT: {result}")
    elif len(sys.argv) >= 3 and sys.argv[1] == "--task-file":
        path = sys.argv[2]
        try:
            with open(path, "r", encoding="utf-8") as f:
                task = json.load(f)
        except Exception as e:
            print(f"Error reading task file {path}: {e}")
            sys.exit(1)

        result = handle_task(task)
        print(json.dumps({"status": "ok", "result": result}, ensure_ascii=False))
    else:
        main_interactive()


if __name__ == "__main__":
    main()