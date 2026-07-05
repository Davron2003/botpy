import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# TOKENNI SHU YERGA QO'YING
TOKEN = "8087794080:AAENIXZIMJNNXIwlUhRdWzKNB_qa3WKGCEs"
bot = telebot.TeleBot(TOKEN, threaded=False)

IMAGE_URL = "https://i.ibb.co/nW7xfMJ/image.png"
GAME_URL = "https://t.me/Zombie_war_bot/Zombiewargame"

app = Flask(__name__)

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
        print(f"Xato: {e}")

# Vercel xabarlarni qabul qiladigan manzil
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Xato so'rov', 403

@app.route('/')
def index():
    return "Bot Webhook tizimida muvaffaqiyatli ishlamoqda!"
