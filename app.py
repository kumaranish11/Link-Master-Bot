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
    return {"status": "healthy", "uptime": "24/7"}

@app.route('/ping')
def ping():
    return "pong"

def run_bot():
    time.sleep(5)  # Wait for Flask to start
    try:
        from bot import PowerfulLinkBot
        bot = PowerfulLinkBot()
        bot.run()
    except Exception as e:
        print(f"Bot error: {e}")

if __name__ == "__main__":
    # Start bot in background thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Start Flask app
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
