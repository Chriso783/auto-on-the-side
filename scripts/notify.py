import os, sys
sys.path.append(os.path.dirname(__file__))
from telegram_notify import notify

if __name__ == "__main__":
    msg = " ".join(sys.argv[1:]) or "Ping"
    print(f"🚀 Starting Telegram notification...")
    print(f"📍 Working directory: {os.getcwd()}")
    print(f"📁 Script directory: {os.path.dirname(__file__)}")
    
    # Check if running in GitHub Actions
    if os.environ.get('GITHUB_ACTIONS'):
        print(f"🏃 Running in GitHub Actions")
        print(f"📦 Repository: {os.environ.get('GITHUB_REPOSITORY', 'unknown')}")
        print(f"🔢 Run number: {os.environ.get('GITHUB_RUN_NUMBER', 'unknown')}")
    
    result = notify(msg)
    
    if result == 200:
        print(f"🎉 Notification completed successfully")
        sys.exit(0)
    elif result == 0:
        print(f"⏭️  Notification skipped (missing credentials)")
        sys.exit(0)
    else:
        print(f"💥 Notification failed with status: {result}")
        sys.exit(1)
