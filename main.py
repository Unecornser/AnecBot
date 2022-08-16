import random
import telebot
import requests
from bs4 import BeautifulSoup as b
URL = "https://www.anekdot.ru/author-best/years/?years=anekdot"
URL2 = "https://www.anekdot.ru/release/anekdot/day/"
URL3 = "https://www.anekdot.ru/last/non_burning/"
URL3 = "https://www.anekdot.ru/last/anekdot_original/"
URL4 = "https://www.anekdot.ru/author-best/years/?years=anekdot"
URL5 = "https://www.anekdot.ru/release/anekdot/month/"
API_KEY = "5611651534:AAGdZGLoGiDMrR6aAloKXyWfIHGnGm_mygY"
r = requests.get(URL)
def parser(url):
    r = requests.get(url)
    soup = b(r.text, "html.parser")
    anek = soup.find_all("div",class_= "text")
    return [c.text for c in anek]

list_of_joke = parser(URL)
list_of_joke += parser(URL2)
list_of_joke += (parser(URL3))
list_of_joke +=(parser(URL5))
list_of_joke += (parser(URL4))
random.shuffle(list_of_joke)
bot = telebot.TeleBot(API_KEY)
print(len(list_of_joke))


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Бот с анеками. Твердо и четко. что бы вывести мем, напиши - /an", parse_mode="html")

@bot.message_handler(commands=["an"])
def jokes(message):
    if message.text.lower() in "/an":
        bot.send_message(message.chat.id,list_of_joke[0])
        del list_of_joke[0]

bot.polling(none_stop=True)
