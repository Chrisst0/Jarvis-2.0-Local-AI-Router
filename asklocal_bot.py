import json
import subprocess
import os

import discord
from discord.ext import commands
from discord import app_commands
from secrets_local import DISCORD_BOT_TOKEN

DISCORD_TOKEN = DISCORD_BOT_TOKEN

# CONFIG
JARVIS_DIR = r"F:\Projects\Jarvis"
TASK_FILE = os.path.join(JARVIS_DIR, "tasks", "current_task.json")
PYTHON_EXE = "python"  # oppure r"C:\Python314\python.exe" se vuoi forzare quello

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


def run_jarvis_ai_chat(prompt: str) -> str:
    # 1) scrivi il JSON del task
    task = {
        "type": "ai.chat",
        "payload": {
            "prompt": prompt,
        },
    }

    os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(task, f, ensure_ascii=False)

    # 2) esegui main.py --task-file ...
    cmd = [
        PYTHON_EXE,
        os.path.join(JARVIS_DIR, "main.py"),
        "--task-file",
        TASK_FILE,
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=JARVIS_DIR,
        timeout=180,
    )

    if result.returncode != 0:
        return f"Errore Jarvis (code {result.returncode}): {(result.stdout or result.stderr).strip()}"

    # 3) stdout è tipo {"status": "ok", "result": "..."}
    try:
        data = json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return f"Output non valido da Jarvis: {result.stdout.strip()}"

    status = data.get("status")
    res = data.get("result", "")
    if status != "ok":
        return f"Jarvis ha risposto con status={status}: {res}"

    return res or "Nessuna risposta."


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id={bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} application commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.command(name="asklocal")
async def asklocal_prefix(ctx: commands.Context, *, prompt: str):
    """Comando classico con !asklocal"""
    await ctx.send("Sto chiedendo a Jarvis (Ollama)...")
    try:
        answer = run_jarvis_ai_chat(prompt)
    except Exception as e:
        await ctx.send(f"Errore eseguendo Jarvis: {e}")
        return

    if len(answer) <= 1900:
        await ctx.send(answer)
    else:
        chunks = []
        current = []
        length = 0
        for line in answer.splitlines():
            if length + len(line) + 1 > 1800:
                chunks.append("\n".join(current))
                current = [line]
                length = len(line)
            else:
                current.append(line)
                length += len(line) + 1
        if current:
            chunks.append("\n".join(current))

        for chunk in chunks:
            await ctx.send(chunk)


@bot.tree.command(name="asklocal", description="Ask local Jarvis (Ollama) a concise question.")
@app_commands.describe(prompt="Your question for local Jarvis")
async def asklocal_slash(interaction: discord.Interaction, prompt: str):
    """Slash command /asklocal"""
    await interaction.response.defer(thinking=True)
    try:
        answer = run_jarvis_ai_chat(prompt)
    except Exception as e:
        await interaction.followup.send(f"Errore eseguendo Jarvis: {e}")
        return

    if len(answer) <= 1900:
        await interaction.followup.send(answer)
    else:
        chunks = []
        current = []
        length = 0
        for line in answer.splitlines():
            if length + len(line) + 1 > 1800:
                chunks.append("\n".join(current))
                current = [line]
                length = len(line)
            else:
                current.append(line)
                length += len(line) + 1
        if current:
            chunks.append("\n".join(current))

        for chunk in chunks:
            await interaction.followup.send(chunk)


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)