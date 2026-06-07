import subprocess
import logging
from typing import Any, Dict

logger = logging.getLogger("jarvis.windows_control")

PS_PATH = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
SCRIPT_PATH = r"F:\Projects\Jarvis\scripts\windows\run_whitelisted.ps1"


def handle_windows_action(task: Dict[str, Any]) -> str:
    """
    task["payload"] deve contenere:
      { "action": "open_vscode" | "open_chrome" | "open_obs" | ... }
    """
    payload = task.get("payload") or {}
    action = payload.get("action")

    if not action:
        return "Missing 'action' in payload."

    logger.info("WindowsControl: requested action=%s", action)

    cmd = [
        PS_PATH,
        "-ExecutionPolicy", "Bypass",
        "-File", SCRIPT_PATH,
        "-Action", action,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except Exception as e:
        logger.exception("Error executing PowerShell script")
        return f"Error invoking PowerShell: {e}"

    stdout = (result.stdout or "").strip()
    stderr = (result.stderr or "").strip()

    logger.info(
        "WindowsControl: exit=%s stdout=%s stderr=%s",
        result.returncode,
        stdout,
        stderr,
    )

    if result.returncode != 0:
        return f"PowerShell error (code {result.returncode}): {stdout or stderr}"

    return stdout or "Action completed."
