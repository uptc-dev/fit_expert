#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py#L87

from app.chat import Chat

chat = Chat()
# ==========================================================
# Vars
age = 0
gender = ''

# ==========================================================
import nlp

def processAge(user_name, message, bot, chat_id):
    result = nlp.findDigits(nlp.clearEmptyWords(nlp.tokenizeText(message)))
    if len(result) == 1:
        if (validateAge(int(result[0]))):
            age = result[0]
            print(age)
            sendMessage('¿A que género perteneces?',chat_id, bot)
        else:
            sendMessage('Talvez no deberias hacer este tipo de deporte con {} años, sin embargo puedes intentar con otra edad'.format(result[0]), chat_id, bot)
            sendMessage('¿Cuantos años tienes?', chat_id, bot)
    elif len(result) > 1:
        sendMessage('Me confundi porque escribiste varios numeros', chat_id, bot)
        sendMessage('¿Cuantos años tienes?', chat_id, bot)
    elif len(result) == 0:
        sendMessage('{}, no escribiste tu edad'.format(user_name), chat_id, bot)
        sendMessage('¿Cuantos años tienes?', chat_id, bot)

def validateAge(age):
    return True if age >= 10 and age <= 100 else False

def processGender(user_name, message, bot, chat_id):
    result = nlp.clearEmptyWords(nlp.tokenizeText(message))
    if (len(result) > 0):
        gender = nlp.findGender(result)
        if (gender != ''):
            print(gender)
            sendMessage('A bueno, ahora quiero preguntarte algo', chat_id, bot)
            sendMessage('¿Como te sientes hoy?', chat_id, bot)
        else:
            sendMessage('Creo que no te he podido entender', chat_id, bot)
            sendMessage('¿A que género perteneces?',chat_id, bot)
    else:
        sendMessage('Creo que no te he podido entender', chat_id, bot)
        sendMessage('¿A que género perteneces?',chat_id, bot)

def processMood(user_name, message, bot, chat_id):
    result = nlp.clearEmptyWords(nlp.tokenizeText(message))
    nlp.moodSentence(result)
    # sendMessage(result, chat_id, bot)

# ==========================================================

"""
https://github.com/python-telegram-bot/python-telegram-bot
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = '338471221:AAFffwfcY0ZHhcsOx-Mqx11wzbeF1pPH4YE'

def start(bot, update):
    chat_id = update.message.chat_id
    chat.setChatId(chat_id)
    user = update.message.from_user
    sendMessage('Hola ' + user.first_name + ', soy un bot experto en entrenamiento físico, puedes preguntarme lo que quieras', chat_id, bot)
    sendMessage('¿Cuantos años tienes?', chat_id, bot)

def listener(bot, update):
    chat_id = update.message.chat_id
    message = (update.message.text).lower()
    user = update.message.from_user
    last_question = lastQuestion(chat_id)
    saveMessage(chat_id, '@' + user.username + ': ' + message)
    if last_question == '_¿cuantos_años_tienes?':
        processAge(user.first_name, message, bot, chat_id)
    elif last_question == '_¿a_que_género_perteneces?':
        processGender(user.first_name, message, bot, chat_id)
    elif last_question == '_¿como_te_sientes_hoy?':
        processMood(user.first_name, message, bot, chat_id)
    else:
        bot.sendMessage(chat_id = chat_id, text = 'No puedo entenderte, /help')

# Send message from bot to the user
def sendMessage(message, chat_id, bot):
    bot.sendMessage(chat_id = chat_id, text = message)
    print(chat.getFilePath())
    chat.saveMessage(message)
    # chat.saveMessage(message)
    # chat.saveMessage(message)
    # saveMessage(chat_id, '@fit_expert_bot: ' + message)

# Returns last question from the bot
def lastQuestion(chat_id):
    return readLastMessage(chat_id)

def main():
    print ("Bot iniciado . . .")

    updater = Updater(token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    listener_handler = MessageHandler([Filters.text], listener)
    dispatcher.add_handler(listener_handler)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
