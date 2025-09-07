import os, sys
sys.path.append(os.path.dirname(__file__))
from telegram_notify import notify

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) or "Ping"
    notify(msg)
