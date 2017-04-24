#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
import telebot
from telebot import types
from nameparser.parser import HumanName
from nltk.tokenize import sent_tokenize, word_tokenize

class Conversation:

    def __init__(self, bot):
        self.bot = bot
        self.chatId = ""
        self.started = False
        self.indexQuestion = 0
        self.name = ""
        self.age = 0
        self.sex = ""
        self.part = ""
        self.experience = ""
        self.place = ""

    def simpleAnswer(self, simpleAnswer):
        self.bot.send_message(self.chatId, simpleAnswer)

    def setChatId(self, chatId):
        self.chatId = chatId

    def genderMarkUp(self):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('man', 'woman')
        return markup

    def experienceMarkUp(self):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('short', 'good', 'long')
        return markup

    def partMarkUp(self):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('biceps', 'back')
        return markup

    def getDifficulty(self):
        if self.experience == 'short':
            difficulty = 'BEGINNER'
        elif self.experience == 'good':
            difficulty = 'INTERMEDIATE'
        elif self.experience == 'long':
            difficulty = 'EXPERT'
        return difficulty

    def increment(self):
        self.indexQuestion += 1

    def getChatId(self):
        return self.chatId

    def setStarted(self, started):
        self.started = started

    def isStarted(self):
        return self.started

    def setIndexQuestion(self, indexQuestion):
        self.indexQuestion = indexQuestion

    def getIndexQuestion(self):
        return self.indexQuestion

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setName(self, text):
        text = text.lower()
        self.name = text.capitalize()

    def getName(self):
        return self.name

    def get_human_age(self, text):
        text = sent_tokenize(text)
