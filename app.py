from flask import Flask, request
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Ultra Advanced LinkMaster Bot is running! ✅"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Bot is running"}

@app.route('/webhook', methods=['POST'])
def webhook():
    return "OK", 200

def run_bot():
    from bot import PowerfulLinkBot
    bot = PowerfulLinkBot()
    bot.run()

if __name__ == "__main__":
    # Start bot in background thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Start Flask app
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
