#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from app.chat import Chat
from app.nlp import NaturalLanguageProcessing
from app.profile import Profile
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = '338471221:AAFffwfcY0ZHhcsOx-Mqx11wzbeF1pPH4YE'
bot_name = 'fit_expert_bot'

chat = Chat()
nlp = NaturalLanguageProcessing()
profile = Profile();

NAME, AGE, MOOD = range(3)

# Send message from bot to the user
def send_message(bot, message):
    bot.send_message(chat_id = chat.get_chat_id(), text = message)
    chat.save_message('@' + bot_name + ': ' + message)
    logger.info('@' + bot_name +' said: ' + message)

# Receive message from user
def receive_message(message):
    chat.save_message('@' + chat.get_user().username + ': ' + message)
    logger.info('@' + chat.get_user().username + ' said: ' + message)

# Start chat with an user
def start(bot, update):
    # user = update.message.from_user
    chat.set_chat_id(update.message.chat_id)
    chat.set_user(update.message.from_user)
    send_message(bot, "Hello, today I'll be your coach, I will hold a conversation with you. Send /cancel to stop talking to me or /skip this question.")
    send_message(bot, 'What is your full name?')
    return NAME

# Ask to user for name
def name(bot, update):
    message = (update.message.text)
    receive_message(message)
    name = nlp.find_human_names(nlp.clear_empty_words(nlp.tokenize_text(message)))
    if (name != False):
        profile.set_name(name)
        profile.set_gender(nlp.find_gender(name))
        send_message(bot, "Oh good, and how old are you?, you can /skip")
        logger.info("User's name is {}, user's gender is {}".format(name, profile.get_gender()))
        return AGE
    else:
        send_message(bot, "Um ,I don't understand you. /skip")
        send_message(bot, 'What is your full name?')
        return NAME

# Skip send name
def skip_name(bot, update):
    receive_message("/skip to send name")
    return AGE

# Ask to user for age
def age(bot, update):
    message = (update.message.text)
    receive_message(message)
    result = nlp.find_digits((nlp.tokenize_text(message.lower())))
    if (len(result) == 1):
        if(nlp.validate_age(result[0])):
            sendMessage(bot, "Ok let's go to workout!, How do you feel today")
            return MOOD
        else:
            sendMessage(bot, "Om, Are you sure to do it? haha, Aren't you too old/young for this?")
            # return CONFIRM_AGE
    elif (len(result) > 1):
        sendMessage(bot, "Haha, I'm confused, you wrote many numbers")
        return AGE
    elif (len(result) == 0):
        sendMessage(bot, "Then you don't want to say me yor age, How old are you?")
        return AGE

# Skip send age
def skip_age(bot, update):
    receive_message("/skip to send age")
    return MOOD

# Ask to user for mood
def mood(bot, update):
    print("Tratar estado animico")

# Skip to send mood
def skip_mood(bot, update):
    receive_message("/skip to send mood")

def cancel(bot, update):
    send_message(bot, "Bye! I hope we can talk again some day.")
    logger.info('User @{} canceled the conversation.'.format(chat.get_user().username))
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
    NAME:[MessageHandler([Filters.text], name),
          CommandHandler('skip', skip_name)],
    AGE:[MessageHandler([Filters.text], age),
         CommandHandler('skip', skip_age)],
    MOOD:[MessageHandler([Filters.text], mood),
          CommandHandler('skip', skip_mood)]
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
