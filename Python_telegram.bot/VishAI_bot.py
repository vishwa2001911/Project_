import telebot 
import openai
import os

f2 = open("api_key.text", "r")
key2 = f2.read()
f2.close()


f = open("key.text", "r")
key = f.read()
f.close()


def ask_ai(q):
    openai.api_key = key2

    answer = openai.Completion.create(  
      model="text-davinci-001",
      prompt=f" {q} :\n\n\n\n\n",
      temperature = 1,
      max_tokens = 300,
      top_p = 1,
      frequency_penalty=0,
      presence_penalty=0

    )
    return answer["choices"][0]["text"]



bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am VishAI Bot.
I am here to chat with you. Just say anything  and I'll answer for that !\
""")
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, ask_ai(message.text))

    
    

    
bot.polling()






