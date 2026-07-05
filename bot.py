import telebot
from flask import Flask, request

# Yangi faol tokening
TOKEN = "8087794080:AAENIXZIMJNNXIwlUhRdWzKNB_qa3WKGCEs"
bot = telebot.TeleBot(TOKEN, threaded=False)

IMAGE_URL = "https://i.ibb.co/nW7xfMJ/image.png"
GAME_URL = "https://t.me/Zombie_war_bot/Zombiewargame"

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    play_button = telebot.types.InlineKeyboardButton(text="🎮 Play", url=GAME_URL)
    markup.add(play_button)
    
    caption_text = (
        "👋 Xush kelibsiz! Zombie War dunyosiga qadam qo'yishga tayyormisiz?\n\n"
        "O'yinni boshlash uchun pastdagi tugmani bosing 👇"
    )
    try:
        bot.send_photo(chat_id=message.chat.id, photo=IMAGE_URL, caption=caption_text, reply_markup=markup)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Telegram faqat shu post manzilga xabar uradi
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Taqiqlangan', 403

@app.route('/', methods=['GET'])
def index():
    return "Bot muvaffaqiyatli ishlamoqda!"
