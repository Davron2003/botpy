import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

TOKEN = "8087794080:AAHTIyjk9Vh9BxPH4ISbpMiiKBhSPuJnMzw"
bot = telebot.TeleBot(TOKEN)

IMAGE_URL = "https://i.ibb.co/nW7xfMJ/image.png"
GAME_URL = "https://t.me/Zombie_war_bot/Zombiewargame"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    play_button = InlineKeyboardButton(text="🎮 Play", url=GAME_URL)
    markup.add(play_button)
    
    caption_text = (
        "👋 Xush kelibsiz! Zombie War dunyosiga qadam qo'yishga tayyormisiz?\n\n"
        "O'yinni boshlash uchun pastdagi tugmani bosing 👇"
    )
    try:
        bot.send_photo(chat_id=message.chat.id, photo=IMAGE_URL, caption=caption_text, reply_markup=markup)
    except Exception as e:
        print(f"Xatolik: {e}")

# Koyeb o'chirib qo'ymasligi uchun soxta veb-server (Port: 8000)
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthCheckHandler)
    server.serve_forever()

if __name__ == "__main__":
    print("Bot va Server ishga tushmoqda...")
    # Veb serverni alohida oqimda yoqamiz
    threading.Thread(target=run_server, daemon=True).start()
    # Botni ishga tushiramiz
    bot.infinity_polling()
