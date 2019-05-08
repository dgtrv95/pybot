import os
import telebot

hostname = "nl.proxyservers.online"
channel = '@pingserver'
token = '657395823:AAEeNxZEgU473zEoT-5_-dk6n1OnZl3oRw0'

response = os.system('ping ' + hostname)
bot = telebot.TeleBot(token)


if response == 0:
  print(hostname + ' is up!')
else:
  print(hostname + ' is down!')
  bot.send_message(channel, hostname + ' is down!')
