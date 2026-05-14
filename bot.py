import os
import telebot
import google.generativeai as genai

# Kalitlarni serverdan olyapmiz
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_KEY')

# Gemini-ni sozlash
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Foydalanuvchi savolini Gemini-ga yuboramiz
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, hozir serverlarimiz biroz band. 1-2 daqiqadan so'ng qayta urinib ko'ring.")

print("Bot ishga tushdi...")
bot.infinity_polling()
