import sys
import json
import urllib.request
from secrets_local import DISCORD_WEBHOOK_URL

WEBHOOK_URL = DISCORD_WEBHOOK_URL

def send_message(content: str) -> None:
    data = {"content": content}

    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 JarvisLocal"
        },
        method="POST",
    )

    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode("utf-8")
        print(f"Status: {resp.status}")
        print(body)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_ds_webhook.py \"message text\"")
        sys.exit(1)

    message = " ".join(sys.argv[1:])
    send_message(message)
