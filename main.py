import random
import telebot
import time

API_TOKEN = '6309037100:AAFz7e8FmI53--cM1s0oR6cXIw1ECcxAyAU'

compliments = [
    "יפה מאוד!",
    "מדהים!",
    "אהבתי את זה!",
    "איזה תמונה מרהיבה!",
    "תמונה מדהימה!"
]

bot = telebot.TeleBot(API_TOKEN)

def format_number(number):
    formatted_number = str(number).zfill(3)
    return formatted_number

@bot.message_handler(content_types=['photo'])
def send_random_compliment_and_number(message):
    random_compliment = random.choice(compliments)
    bot.reply_to(message, random_compliment)

    loading_message = bot.send_message(message.chat.id, "טוען מספר רנדומלי...")
    
    time.sleep(2)
    
    random_number = random.randint(0, 999)
    formatted_number = format_number(random_number)
    bot.send_message(message.chat.id, f"מספר רנדומלי: {formatted_number}")

    bot.delete_message(message.chat.id, loading_message.message_id)

bot.polling()