# Telegram Bot Setup Guide

This repository includes Telegram notifications for workflow status updates. Follow these steps to set up your Telegram bot:

## Step 1: Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` to create a new bot
3. Follow the prompts to name your bot
4. Save the **Bot Token** (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Step 2: Get Your Chat ID

### For Private Messages:
1. Send a message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Look for the `chat.id` value in the response

### For Group/Channel:
1. Add your bot to the group/channel
2. Send a message mentioning the bot: `@yourbotname hello`
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for the `chat.id` value (usually negative for groups)

### Alternative Method:
Use `@userinfobot` or `@RawDataBot` - forward a message from your target chat to get the chat ID.

## Step 3: Add GitHub Secrets

In your GitHub repository:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add these repository secrets:
   - `TELEGRAM_BOT_TOKEN`: Your bot token from Step 1
   - `TELEGRAM_CHAT_ID`: Your chat ID from Step 2

## Step 4: Test the Setup

The heartbeat workflow runs weekly and can be triggered manually:

1. Go to **Actions** → **Heartbeat** → **Run workflow**
2. Check the workflow logs for success/error messages
3. You should receive a Telegram message if everything is configured correctly

## Troubleshooting

### Common Issues:

1. **"Bot token format looks incorrect"**
   - Remove any "bot" prefix from your token
   - Ensure format is: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

2. **"Chat not found" or "Forbidden"**
   - Make sure you've sent at least one message to the bot (for private chats)
   - For groups: ensure the bot is added and has send message permissions

3. **"TELEGRAM_* secrets not set"**
   - Check that your GitHub secrets are named exactly: `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`
   - Secrets are case-sensitive

4. **Workflow fails with "No such file or directory"**
   - The repository checkout and Python setup steps are now included in the workflow

### Testing Locally:

You can test the Telegram notification locally:

```bash
# Set your credentials (replace with actual values)
export TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
export TELEGRAM_CHAT_ID="123456789"

# Test the notification
python scripts/notify.py "Test message from local setup"
```

### Workflow Schedule:

- **Heartbeat**: Runs every Sunday at midnight UTC (`0 0 * * 0`)
- **Manual trigger**: Available via GitHub Actions UI

The notifications will include:
- ✅ Success messages when workflows complete successfully
- ❌ Failure messages when workflows fail
- Repository name and run number for tracking