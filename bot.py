import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "WELCOME TO RYZEN ESCROW BOT\n\n"
        "ALWAYS TRUSTED AND SAFE DEALS WITH RYZEN ESCROW\n\n"
        "OWNER - @RYZEN_HEREE\n"
        "MAIN ESCROW - @RYZEN_ESCROW\n"
        "PROOFS - @RYZEN_ESCROW_DEALS\n"
        "VERIFIED ESCROWER - @RYZEN_ESCROWERS"
    )

bot.infinity_polling()
