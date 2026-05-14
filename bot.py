import os
import threading
from flask import Flask
from telebot import TeleBot  # yoki siz ishlatayotgan kutubxona

# 1. Render uchun kichik Veb-server qismi
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    # Render avtomat beradigan portni oladi, bo'lmasa 8080 ni ishlatadi
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.daemon = True # Bot to'xtasa, bu ham to'xtashi uchun
    t.start()

# 2. Botni sozlash (O'zgaruvchilarni Dashboard'dan oladi)
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

# --- BOTINGIZNING ASOSIY KODI SHU YERDAN BOSHLANADI ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men ishlayapman.")

# --- BOTNI ISHGA TUSHIRISH ---
if __name__ == "__main__":
    keep_alive()  # Avval veb-serverni alohida oqimda yoqamiz
    print("Bot ishga tushdi...")
    bot.infinity_polling() # Keyin botni cheksiz so'rovga qo'yamiz
