#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from app.chat import Chat
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = '338471221:AAFffwfcY0ZHhcsOx-Mqx11wzbeF1pPH4YE'
bot_name = 'fit_expert_bot'
chat = Chat()

NAME = range(4)

# Send message from bot to the user
def send_message(bot, message):
    bot.send_message(chat_id = chat.getChatId(), text = message)
    chat.save_message('@' + bot_name + message)
    logger.info('@' + bot_name +' said: ' + message)

def receive_message(message):
    chat.save_message('@' + chat.getUser().username + ': ' + message)
    logger.info('@' + chat.getUser().username + ' said: ' + message)

def start(bot, update):
    # user = update.message.from_user
    chat.setChatId(update.message.chat_id)
    chat.setUser(update.message.from_user)
    send_message(bot, "Hello, today I'll be your coach, I will hold a conversation with you. Send /cancel to stop talking to me.")
    send_message(bot, 'What is your name?')
    return NAME

def name(bot, update):
    message = (update.message.text).lower()
    receive_message(message)


def cancel(bot, update):
    send_message(bot, "Bye! I hope we can talk again some day.")
    logger.info('User {} canceled the conversation.'.format(chat.getUserName()))
    return ConversationHandler.END

def error(bot, update, error):
    logger.warn('Update "{}" caused error "{}"'.format(update, error))


def main():
    logger.info('Bot started')

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states
    conversation_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],
    states = {
    NAME:[MessageHandler([Filters.text], name)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conversation_handler)

    # log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
