
import telebot
from telebot import types
import random

TOKEN ="8922366786:AAF3g6QssVJI-ZD_agAJW3PihsOWKLfoVY4"
 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    menu = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    menu.row("🇺🇿 O‘zbekiston tarixi")
    menu.row("🌍 Jahon tarixi", "👑 Buyuk shaxslar")
    menu.row("📅 Tarixiy sanalar", "🧠 Tarixiy viktorina")

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum!\n"
        "🏛 Buyuk Ajdodlar botiga xush kelibsiz!\n\n"
        "Kerakli bo‘limni tanlang:",
        reply_markup=menu
    )

@bot.message_handler(func=lambda m: m.text == "🇺🇿 O‘zbekiston tarixi")
def uzbek_tarix(message):
    bot.send_message(
        message.chat.id,
        "🇺🇿 O‘ZBEKISTON TARIXI\n\n"
        "• Qadimgi Xorazm\n"
        "• Kushon davlati\n"
        "• Somoniylar davlati\n"
        "• Amir Temur va Temuriylar\n"
        "• O‘zbekiston mustaqilligi"
    )

@bot.message_handler(func=lambda m: m.text == "🌍 Jahon tarixi")
def jahon_tarix(message):
    bot.send_message(
        message.chat.id,
        "🌍 JAHON TARIXI\n\n"
        "• Qadimgi Misr\n"
        "• Qadimgi Yunoniston\n"
        "• Rim imperiyasi\n"
        "• O‘rta asrlar\n"
        "• Jahon urushlari"
    )

@bot.message_handler(func=lambda m: m.text == "👑 Buyuk shaxslar")
def shaxslar(message):
    bot.send_message(
        message.chat.id,
        "👑 BUYUK SHAXSLAR\n\n"
        "• Amir Temur\n"
        "• Mirzo Ulug‘bek\n"
        "• Zahiriddin Muhammad Bobur\n"
        "• Alisher Navoiy\n"
        "• Abu Ali ibn Sino"
    )

@bot.message_handler(func=lambda m: m.text == "📅 Tarixiy sanalar")
def sanalar(message):
    bot.send_message(
        message.chat.id,
        "📅 MUHIM TARIXIY SANALAR\n\n"
        "1370-yil — Amir Temur hokimiyat tepasiga keldi.\n"
        "1441-yil — Alisher Navoiy tug‘ildi.\n"
        "1483-yil — Zahiriddin Muhammad Bobur tug‘ildi.\n"
        "1991-yil 1-sentabr — O‘zbekiston mustaqilligi e’lon qilindi."
    )

@bot.message_handler(func=lambda m: m.text == "🧠 Tarixiy viktorina")
def viktorina(message):
    savollar = [
        ("Amir Temur davlatining poytaxti qaysi shahar edi?",
         ["Samarqand", "Buxoro", "Xiva"], "Samarqand"),
        ("Mirzo Ulug‘bek kim bo‘lgan?",
         ["Astronom va hukmdor", "Shoir", "Sayyoh"], "Astronom va hukmdor"),
        ("O‘zbekiston mustaqilligi qachon e’lon qilingan?",
         ["1991-yil", "1992-yil", "1990-yil"], "1991-yil")
    ]

    savol, variantlar, javob = random.choice(savollar)
    bot.send_message(message.chat.id, savol)

    menu = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    for variant in variantlar:
        menu.add(variant)

    bot.send_message(
        message.chat.id,
        "Javobni tanlang:",
        reply_markup=menu
    )

    bot.register_next_step_handler(
        message, tekshir, javob
    )

def tekshir(message, javob):
    if message.text == javob:
        bot.send_message(message.chat.id, "✅ To‘g‘ri javob!")
    else:
        bot.send_message(
            message.chat.id,
            "❌ Noto‘g‘ri. To‘g‘ri javob: " + javob
        )

    start(message)

bot.infinity_polling()
      
