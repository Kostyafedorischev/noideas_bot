import telebot
from bot_main.keyboards_ni import main_menu, cases_menu, services_menu, socials_menu, text_menu
from appeals import ask_name
from bot_main import bot
import json
import os  # Добавлен импорт модуля os
from telebot import types

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите пункт меню:", reply_markup=main_menu())

# Обработчик inline-кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'about':
        about_text = ("no ideas — коммуникационное агентство. "
                      "У нас много идей, которые мы готовы реализовать вместе с вами. "
                      "Мы — молодая команда, которая имеет опыт в маркетинге и дизайне более 5 лет. "
                      "Наша миссия — качественно реализовывать маркетинговые и креативные стратегии для брендов, "
                      "которым это действительно нужно.")
        bot.edit_message_text(
            chat_id=call.message.chat.id, message_id=call.message.message_id, text=about_text,
            reply_markup=text_menu()
        )

    elif call.data == 'cases':
        bot.edit_message_text(
            chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите кейс:",
            reply_markup=cases_menu()
        )

    elif call.data == 'back_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите пункт меню:", reply_markup=main_menu())

    elif call.data == 'contact':
        ask_name(call.message)

    # Новое меню "Услуги"
    elif call.data == 'services':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите услугу:", reply_markup=services_menu())

    # Пункты внутри меню "Услуги"
    elif call.data == 'design':
        # Отправляем PDF файл в ответ на выбор "Дизайн"
        with open('bot_main/no ideas – Услуги по дизайну.pdf', 'rb') as pdf_file:
            bot.send_document(call.message.chat.id, pdf_file)
        bot.send_message(call.message.chat.id, "Наш PDF-файл с услугами по дизайну", reply_markup=text_menu())


# Запуск бота
bot.polling(none_stop=True)