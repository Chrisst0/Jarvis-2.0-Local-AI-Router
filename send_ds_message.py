import sys
import json
import urllib.request
from urllib.error import HTTPError
from secrets_local import BOT_TOKEN

BOT_TOKEN = BOT_TOKEN
CHANNEL_ID = "1085574291770322994"


def send_message(content: str) -> None:
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    data = {"content": content}

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bot {BOT_TOKEN}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            print(f"Status: {resp.status}")
            print(body)
    except HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"HTTPError: {e.code} {e.reason}")
        print(err_body)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_ds_message.py \"message text\"")
        sys.exit(1)

    message = " ".join(sys.argv[1:])
    send_message(message)
