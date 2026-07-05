import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

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

# Hugging Face-da ishga tushirish uchun oddiy interfeys
import gradio as io

def greet():
    return "Zombie War Bot 24/7 faol holatda!"

# Botni alohida oqimda orqada yuritish
import threading
threading.Thread(target=lambda: bot.infinity_polling(), daemon=True).start()

# Asosiy sahifani ishga tushirish (Hugging Face uchun)
demo = io.Interface(fn=greet, inputs=[], outputs="text", title="Zombie War Bot Status")
demo.launch(server_name="0.0.0.0", server_port=7860)
