import os
import urllib.parse
import urllib.request
import urllib.error
import json

def notify(message: str) -> int:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    
    if not token:
        print("❌ TELEGRAM_BOT_TOKEN not set; skipping notify")
        return 0
    if not chat_id:
        print("❌ TELEGRAM_CHAT_ID not set; skipping notify")
        return 0
    
    print(f"📤 Sending Telegram message to chat_id: {chat_id}")
    print(f"📝 Message: {message}")
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id, 
        "text": message,
        "parse_mode": "HTML"
    }).encode("utf-8")
    
    req = urllib.request.Request(
        url, 
        data=data, 
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            response_data = resp.read().decode('utf-8')
            
            if status == 200:
                print(f"✅ Telegram message sent successfully (status: {status})")
                try:
                    result = json.loads(response_data)
                    if result.get('ok'):
                        print(f"📨 Message ID: {result.get('result', {}).get('message_id', 'unknown')}")
                    else:
                        print(f"⚠️ Telegram API returned ok=false: {result}")
                except json.JSONDecodeError:
                    print(f"⚠️ Could not parse response as JSON: {response_data}")
            else:
                print(f"⚠️ Unexpected status code: {status}")
                print(f"📄 Response: {response_data}")
            
            return status
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        try:
            error_response = e.read().decode('utf-8')
            print(f"📄 Error response: {error_response}")
            try:
                error_json = json.loads(error_response)
                if 'description' in error_json:
                    print(f"💬 Telegram error: {error_json['description']}")
            except json.JSONDecodeError:
                pass
        except Exception as ex:
            print(f"Could not read error response: {ex}")
        return e.code
        
    except urllib.error.URLError as e:
        print(f"❌ URL Error: {e.reason}")
        return 0
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 0
