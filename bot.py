import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot tokeningiz
TOKEN = "8087794080:AAHTIyjk9Vh9BxPH4ISbpMiiKBhSPuJnMzw"
bot = telebot.TeleBot(TOKEN)

# Rasm va O'yin URL manzillari
IMAGE_URL = "https://i.ibb.co/nW7xfMJ/image.png"
GAME_URL = "https://t.me/Zombie_war_bot/Zombiewargame"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Inline tugma yaratish (Play tugmasi WebApp yoki URL sifatida ochiladi)
    markup = InlineKeyboardMarkup()
    play_button = InlineKeyboardButton(text="🎮 Play", url=GAME_URL)
    markup.add(play_button)
    
    # Bot foydalanuvchiga yuboradigan matn
    caption_text = (
        "👋 Xush kelibsiz! Zombie War dunyosiga qadam qo'yishga tayyormisiz?\n\n"
        "O'yinni boshlash uchun pastdagi tugmani bosing 👇"
    )
    
    # Rasm va uning tagida matn + tugmani yuborish
    try:
        bot.send_photo(
            chat_id=message.chat.id, 
            photo=IMAGE_URL, 
            caption=caption_text, 
            reply_markup=markup,
            parse_mode="Markdown"
        )
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# Botni uzluksiz ishga tushirish
if __name__ == "__main__":
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.infinity_polling()