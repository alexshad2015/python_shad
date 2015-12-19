# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:41:32 2015

@author: Alexander
"""

import telebot
from telebot import types
import requests
from BeautifulSoup import BeautifulSoup as bs
from urllib2 import urlopen as open
import re


token = 'bot_token'

if __name__ == "__main__":
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_start(message):
        bot.send_message(message.chat.id, "Hi, is /help needed?")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        help_ = []
        help_.append("I'm an InfoBot.\n")
        help_.append("/start - Hello;\n")
        help_.append("/help - display all commands;\n")
        help_.append("/menu - show all selections by buttons;\n")
        help_.append("/football - print top english football club with scores;\n")
        help_.append("/weather - display weather in Moscow for several days;\n")
        help_.append("/brent - display current price for brent oil;\n")
        bot.send_message(message.chat.id, "".join(help_), parse_mode="Markdown")

    @bot.message_handler(commands=['weather'])
    def get_weather(message):
        url = "http://api.wunderground.com/api/0def10027afaebb7/forecast/q/Russia/Moscow.json"
        req = requests.get(url)
        data = req.json()
        out = []
        for day in data['forecast']['simpleforecast']['forecastday']:
            out.append('\n' + str(day['date']['weekday']) + ":" + '\n')
            out.append("Conditions: " + str(day['conditions']) + '\n')
            out.append("High: " + str(day['high']['celsius']) + "C" + '\n' "Low: ")
            out.append(str(day['low']['celsius']) + "C" + '\n')
        bot.send_message(message.chat.id, " ".join(out), parse_mode="Markdown")

    @bot.message_handler(commands=['football'])
    def get_result_table(message):
        pattern = r"(?<=\>).+?(?=\<)"
        out = []
        url = 'http://www.supersport.com/football/barclays-premier-league/logs'
        s = bs(open(url).read())
        number_of_commands = [2, 3, 4]
        for i in number_of_commands:
            c = s('table')[0].findAll('tr')[i].findAll('td')[1]
            b = s('table')[0].findAll('tr')[i].findAll('td')[9]
            out.append('\n' + str(re.findall(pattern, str(c)))[2:-2] + ":" + '\n')
            out.append(str(re.findall(pattern, str(b)))[2:-2])
        bot.send_message(message.chat.id, " ".join(out), parse_mode="Markdown")

    @bot.message_handler(commands=['brent'])
    def get_brent_price(message):
        pattern = r"(?<=\>).+?(?=\<)"
        out = ['Brent Price Now :']
        url = bs(open('http://www.bloomberg.com/energy').read())
        c = url('table')[0].findAll('tr')[2].findAll('td')[2]
        out.append('\n' + str(re.findall(pattern, str(c)))[2:-2] + '\n')
        bot.send_message(message.chat.id, " ".join(out), parse_mode="Markdown")

    @bot.message_handler(commands=['menu'])
    def send_menu(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Help', 'Brent price', 'Weather', 'Football Result')
        msg = bot.reply_to(message, "Menu", reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)

    def process_step(message):
        if message.text == 'Help':
            send_help(message)
        if message.text == 'Weather':
            get_weather(message)
        if message.text == 'Football Result':
            get_result_table(message)
        if message.text == 'Brent price':
            get_brent_price(message)

    bot.polling(none_stop=True)
