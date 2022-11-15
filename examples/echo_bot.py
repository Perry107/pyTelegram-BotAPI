#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import time
import board
import digitalio



 
enable_pin = digitalio.DigitalInOut(board.D18)
coil_A_1_pin = digitalio.DigitalInOut(board.D14)
coil_A_2_pin = digitalio.DigitalInOut(board.D15)
coil_B_1_pin = digitalio.DigitalInOut(board.D23)
coil_B_2_pin = digitalio.DigitalInOut(board.D24)
 
enable_pin.direction = digitalio.Direction.OUTPUT
coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT
 
enable_pin.value = True
 
def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
 
        i += 1
 
def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(0, 0, 1, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        i += 1
 
def setStep(w1, w2, w3, w4):
    coil_A_1_pin.value = w1
    coil_A_2_pin.value = w2
    coil_B_1_pin.value = w3
    coil_B_2_pin.value = w4
 
def mover():
    user_delay=10 
    user_steps=100 
    forward(int(user_delay) / 1000.0, int(user_steps))
    
    backwards(int(user_delay) / 1000.0, int(user_steps))













API_TOKEN = '5466706717:AAHiTWh6y0DdJZR7tgWz6hEXBo9Ycjr2v3k'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot107.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


    #Codigo adicional
    mover()

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
