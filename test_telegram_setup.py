#!/usr/bin/env python3
"""
Telegram Bot Setup Validator
Test script to help diagnose Telegram bot configuration issues
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

try:
    from telegram_notify import notify
except ImportError:
    print("❌ Could not import telegram_notify module")
    print("Make sure you're running this from the repository root directory")
    sys.exit(1)

def test_telegram_setup():
    print("🔍 Testing Telegram bot setup for auto-on-the-side...")
    print("=" * 60)
    
    # Test 1: Check environment variables
    print("\n1️⃣  Checking environment variables:")
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    
    if token:
        print(f"   ✅ TELEGRAM_BOT_TOKEN is set (length: {len(token)} chars)")
        
        # Validate token format
        if token.startswith('bot'):
            print("   ⚠️  Warning: Bot token starts with 'bot' - remove this prefix")
            print("      Example: Use '123456789:ABC...' not 'bot123456789:ABC...'")
        
        if ':' not in token:
            print("   ❌ Error: Bot token format is incorrect")
            print("      Expected format: '123456789:ABCdefGHIjklMNOpqrsTUVwxyz'")
        else:
            parts = token.split(':')
            if len(parts) != 2 or not parts[0].isdigit():
                print("   ⚠️  Warning: Bot token format looks unusual")
                print("      Expected format: 'NUMBER:ALPHANUMERIC'")
            else:
                print(f"   ✅ Token format looks correct (Bot ID: {parts[0]})")
    else:
        print("   ❌ TELEGRAM_BOT_TOKEN is not set")
        print("      Get your token from @BotFather on Telegram")
    
    if chat_id:
        print(f"   ✅ TELEGRAM_CHAT_ID is set: {chat_id}")
        
        # Validate chat ID format
        if chat_id.startswith('-100'):
            print("   ℹ️  This appears to be a supergroup/channel ID")
        elif chat_id.startswith('-'):
            print("   ℹ️  This appears to be a regular group chat ID")
        elif chat_id.isdigit():
            print("   ℹ️  This appears to be a private chat ID")
        else:
            print("   ⚠️  Warning: Chat ID format looks unusual")
            print("      Expected: numeric value (positive for users, negative for groups)")
    else:
        print("   ❌ TELEGRAM_CHAT_ID is not set")
        print("      Send a message to your bot, then visit:")
        print("      https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates")
    
    print("\n2️⃣  Environment setup check:")
    if 'GITHUB_ACTIONS' in os.environ:
        print("   🏃 Running in GitHub Actions environment")
        print(f"   📦 Repository: {os.environ.get('GITHUB_REPOSITORY', 'unknown')}")
        print(f"   🔢 Run number: {os.environ.get('GITHUB_RUN_NUMBER', 'unknown')}")
    else:
        print("   💻 Running in local environment")
    
    # Test 2: Try sending a message
    print("\n3️⃣  Testing message delivery:")
    if token and chat_id:
        print("   🚀 Attempting to send test message...")
        test_msg = "🧪 Test message from auto-on-the-side repository setup validator"
        result = notify(test_msg)
        
        if result == 200:
            print("   🎉 SUCCESS: Test message sent successfully!")
            print("   Check your Telegram chat for the test message.")
        elif result == 0:
            print("   ⏭️  SKIPPED: Missing credentials (this shouldn't happen)")
        else:
            print(f"   ❌ FAILED: Message send failed with status code: {result}")
            print("   Check the error messages above for details.")
    else:
        print("   ⏭️  SKIPPED: Cannot test - missing credentials")
    
    # Test 3: Repository structure check
    print("\n4️⃣  Repository structure check:")
    required_files = [
        'scripts/telegram_notify.py',
        'scripts/notify.py',
        '.github/workflows/heartbeat.yml'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - MISSING")
    
    print("\n" + "=" * 60)
    print("🔧 SETUP INSTRUCTIONS:")
    print("\nIf you need to set up your Telegram bot:")
    print("1. Create bot: Message @BotFather on Telegram, send /newbot")
    print("2. Get chat ID: Send message to bot, then visit getUpdates URL")
    print("3. Add GitHub secrets: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID")
    print("4. Test: Run GitHub Actions 'Heartbeat' workflow manually")
    print("\nFor detailed instructions, see: TELEGRAM_SETUP.md")
    
    print("\n🧪 MANUAL TESTING:")
    print("To test with your own credentials:")
    print("TELEGRAM_BOT_TOKEN='your_token' TELEGRAM_CHAT_ID='your_chat_id' python test_telegram_setup.py")

if __name__ == "__main__":
    test_telegram_setup()