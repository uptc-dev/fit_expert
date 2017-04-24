#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
class Tools:
    def messageToLower(message):
        text = message.text
        return text.lower()
