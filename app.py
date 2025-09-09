from flask import Flask
import threading
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Ultra Advanced LinkMaster Bot is running! ✅"

@app.route('/health')
def health():
    return "OK"

def run_bot():
    # Bot start होने के लिए थोड़ा wait करें
    time.sleep(3)
    try:
        print("🚀 Starting bot...")
        from bot import PowerfulLinkBot
        bot = PowerfulLinkBot()
        print("✅ Bot instance created")
        bot.run()
    except Exception as e:
        print(f"❌ Bot error: {e}")

if __name__ == "__main__":
    print("🔄 Starting Flask and Bot...")
    
    # Bot को background में start करें
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    print("📱 Bot thread started")
    
    # Flask app start करें
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
