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
chat = Chat()

NAME = range(4)

# Send message from bot to the user
def sendMessage(bot, message):
    bot.sendMessage(chat_id = chat.getChatId(), text = message)
    chat.saveMessage('@fit_expert_bot: ' + message)
    logger.info('@fit_expert_bot said: ' + message)

def start(bot, update):
    user = update.message.from_user
    chat.setChatId(update.message.chat_id)
    chat.setUserName(user.first_name)
    sendMessage(bot, "Hello, today I'll be your coach, I will hold a conversation with you. Send /cancel to stop talking to me.")
    return NAME

def name(bot, update):
    print('name')

def cancel(bot, update):
    sendMessage(bot, "Bye! I hope we can talk again some day.")
    logger.info('User {} canceled the conversation.'.format(chat.getUserName()))
    return ConversationHandler.END

def error(bot, update, error):
    logger.warn('Update "{}" caused error "{}"'.format(update, error))


def main():
    logger.info('Bot iniciado')

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
