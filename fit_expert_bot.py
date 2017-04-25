#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read all messages in the chat
def readChat(chat_id):
    file_name = 'docs/{}.txt'.format(chat_id)
    file = open(file_name, 'r')
    chat = file.readlines()
    file.close()
    return chat

# Save all new messages in the chat
def saveMessage(chat_id, message):
    file_name = 'docs/{}.txt'.format(chat_id)
    file = open(file_name, 'a')
    file.write(message + '\n')
    file.close()

# Read last line in the chat
def readLastMessage(chat_id):
    chat = readChat(chat_id)

    return chat[len(chat) - 1]

"""
https://github.com/python-telegram-bot/python-telegram-bot
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = '338471221:AAFffwfcY0ZHhcsOx-Mqx11wzbeF1pPH4YE'

def start(bot, update):
    chat_id = update.message.chat_id
    user = update.message.from_user
    bot.sendMessage(chat_id = chat_id, text = 'Hola ' + user.first_name + ', soy un bot experto en entrenamiento físico, puedes preguntarme lo que quieras')
    message = '¿Cuantos años tienes?'
    bot.sendMessage(chat_id = chat_id, text = message)
    saveMessage(chat_id, '@fit_expert_bot: ' + message)

def listener(bot, update):
    chat_id = update.message.chat_id
    message = (update.message.text).lower()
    user = update.message.from_user
    question_id = questionId(chat_id)
    # saveMessage(chat_id, '@' + user.username + ': ' + message)
    # print(user)
    # saveMessage(chat_id, )
    # messageId(chat_id)

def questionId(chat_id):
    last_message = readLastMessage(chat_id);
    print(last_message)

# def messageId(chat_id):
#     pass
    # lastMessage = readLastMessageConversation(id)
    # print("message Id")
    # last_message = readLastMessageConversation(chat_id)
    # print(last_message)
    # if last_message == "¿Como te llamas?":
    #     print ("Mensaje de como te llamas")
    # elif last_message == "hola":
    #     print ("last message")
    # print (lastMessage)


def main():
    print ("Bot iniciado . . .")
    updater = Updater(token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    listener_handler = MessageHandler([Filters.text], listener)
    dispatcher.add_handler(listener_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

# Token único, lo asigna BotFather cada vez que se crea un nuevo bot.







# # Diferentes comandos para iniciar una conversacion con el Bot.
# @bot.message_handler(commands=['start', 'inicio', 'hola'])
# def send_welcome(message):
#     conversation.setChatId(message.chat.id)
#     conversation.simpleAnswer("Hello and Welcome to Crossfit Recommender Bot. If you want to know more send /help")
#     conversation.simpleAnswer("What is your name?")
#     conversation.setStarted(True)
#     bot.register_next_step_handler(message, process_name)























# import telebot
# from telebot import types
# from config.Database import Database
# from app.Conversation import Conversation
#
# # Token unico, lo asigna BotFather cada vez que se crea un nuevo bot.
# token = "296954471:AAFgdOMweO0ShcEBeIbRFgU0v1VyzHeV5uk"
# bot = telebot.TeleBot(token)
#
# """
# |Atributos de conexion con la base de datos.
# |Para que se pueda conectar al localhost se debe ingresar con la direccion completa 127.0.0.1 .
# """
# DB_HOST = '127.0.0.1'
# DB_USER = 'sr_db'
# DB_PASS = 'sr_db'
# DB_NAME = 'sr_db'
#
# # Database connection.
# database = Database(DB_HOST, DB_USER, DB_PASS, DB_NAME)
# # Instancia de la clase Conversation
# conversation = Conversation(bot)
#
# # Diferentes comandos para iniciar una conversacion con el Bot.
# @bot.message_handler(commands=['start', 'inicio', 'hola'])
# def send_welcome(message):
#     conversation.setChatId(message.chat.id)
#     conversation.simpleAnswer("Hello and Welcome to Crossfit Recommender Bot. If you want to know more send /help")
#     conversation.simpleAnswer("What is your name?")
#     conversation.setStarted(True)
#     bot.register_next_step_handler(message, process_name)
#
# # Guarda el nombre del usuario.
# def process_name(message):
#     try:
#         conversation.setName(message.text)
#         conversation.simpleAnswer("Hello " + conversation.getName() + ", how old are you?")
#         bot.register_next_step_handler(message, process_age)
#     except Exception as e:
#         bot.reply_to(message, "Ops! I can't understand you.")
#
# # Guarda la edad del usuario.
# def process_age(message):
#     try:
#         age = message.text
#         if not age.isdigit():
#             bot.reply_to(message, 'Age should be a number. How old are you?')
#             bot.register_next_step_handler(message, process_age)
#             return
#         conversation.age = age
#         bot.send_message(conversation.chatId, 'You are ...', reply_markup=conversation.genderMarkUp())
#         bot.register_next_step_handler(message, process_sex)
#     except Exception as e:
#         bot.reply_to(message, "Ops! I can't understand you.")
#
# # Guarda el genero del usuario.
# def process_sex(message):
#     try:
#         sex = message.text
#         sex = sex.lower()
#         if (sex == u'man') or (sex == u'woman'):
#             conversation.sex = sex
#             bot.send_message(conversation.chatId, "How long have you been training?\nShort time: Less than 6 months\nGood time: Between 6 and 2 years.\nLong time: More than 2 years.", reply_markup=conversation.experienceMarkUp())
#             bot.register_next_step_handler(message, process_experience)
#         else:
#             bot.send_message(conversation.chatId, "I didn't understand. You are ...", reply_markup=conversation.genderMarkUp())
#             bot.register_next_step_handler(message, process_sex)
#     except Exception as e:
#         bot.reply_to(message, "Ops! I can't understand you.")
#
# def process_experience(message):
#     try:
#         experience = message.text
#         experience = experience.lower()
#         if (experience == u'short') or (experience == u'good') or (experience == u'long'):
#             conversation.experience = experience
#             bot.send_message(conversation.chatId, conversation.name + " , wich part of your body do you like to train more?", reply_markup=conversation.partMarkUp())
#             bot.register_next_step_handler(message, process_part)
#         else:
#             bot.reply_to(message, "Ops! I can't understand you.")
#             bot.send_message(conversation.chatId, "How long have you been training?\nShort time: Less than 6 months\nGood time: Between 6 and 2 years.\nLong time: More than 2 years.", reply_markup=conversation.experienceMarkUp())
#             bot.register_next_step_handler(message, process_experience)
#     except Exception as e:
#         bot.reply_to(message, "Ops! I can't understand you.")
#
# def process_part(message):
#     try:
#         part = message.text
#         part = part.upper()
#         if (part == u'BICEPS') or (part == u'BACK'):
#             conversation.part = part
#             bot.send_message(conversation.chatId, conversation.name + ", are you in home or gym?")
#             bot.register_next_step_handler(message, process_place)
#         else:
#             bot.reply_to(message, "Ops! I can't understand you.")
#             bot.send_message(conversation.chatId, conversation.name + " , wich part of your body do you like to train more?", reply_markup=conversation.partMarkUp())
#             bot.register_next_step_handler(message, process_part)
#     except Exception as e:
#         bot.reply_to(message, "Ops! I can't understand you.")
#
# def process_place(message):
#     place = message.text
#     place = place.lower()
#     difficulty = conversation.getDifficulty()
#     if place == 'home':
#         query = "SELECT name_move, link FROM data WHERE MAIN_MUSCLE='" + conversation.part + "' AND difficulty ='"+ difficulty + "' AND equipment_1='BODY ONLY'"
#     elif place == 'gym':
#         query = "SELECT name_move, link FROM data WHERE MAIN_MUSCLE='" + conversation.part + "' AND difficulty ='"+ difficulty + "' AND equipment_1!='BODY ONLY'"
#     else:
#         bot.reply_to(message, "Ops! I can't understand you.")
#         bot.send_message(conversation.chatId, conversation.name + ", are you in home or gym?")
#         bot.register_next_step_handler(message, process_place)
#
#     consultas = database.executeQuery(query)
#     if consultas != '':
#         bot.send_message(conversation.chatId, "You could do it:")
#         bot.send_message(conversation.chatId, consultas[0])
#         bot.send_message(conversation.chatId, "if you don't know how to do it:")
#         bot.send_message(conversation.chatId, consultas[1])
#         bot.send_message(conversation.chatId, "Bye")
#     else:
#         bot.send_message(conversation.chatId, "No podemos recomendar")
#
#
#
# @bot.message_handler(commands=['help', 'ayuda', 'auxilio', 'no entiendo'])
# def command_help(message):
#     bot.send_message(message.chat.id, "These are the possible comands:\n/start: Start bot.\n")
#
#
#
#




#https://github.com/eternnoir/pyTelegramBotAPI#methods
# https://www.crossfit.com/exercisedemos/
#http://unmonoqueteclea.es/2016/01/01/creando-nuestro-primer-bot-en-telegram/
#http://unmonoqueteclea.es/2016/01/17/creando-nuestro-primer-bot-de-telegram-en-python-2/
#http://librosweb.es/libro/python/capitulo_12/conectarse_a_la_base_de_datos_y_ejecutar_consultas.html
#http://codehero.co/python-desde-cero-bases-de-datos/
#https://www.youtube.com/watch?v=CZ450sbYLus

# """ A message handler is a function that is decorated with the message_handler decorator of a TeleBot instance.
#  Message handlers consist of one or multiple filters. Each filter much return True for a certain message in
#  order for a message handler to become eligible to handle that message. A message handler is declared in the
#  following way (provided bot is an instance of TeleBot. """
#
#
# bot.polling()
# #Infinite loop
# while True:
#     pass
