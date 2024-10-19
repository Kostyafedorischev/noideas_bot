from bot_main import bot, ADMIN_CHAT_ID

# Хранение данных пользователя
user_data = {}

# Процесс сбора заявки
def ask_name(message):
    bot.send_message(message.chat.id, "Чтобы мы могли связаться с вами, нам нужно узнать немного "
                                      "вводной информации. Не переживайте, это быстро, всего 4 вопроса! "
                                      "Для начала – как вас зовут?"
                     )
    bot.register_next_step_handler(message, ask_nickname)

def ask_nickname(message):
    user_data['name'] = message.text
    bot.send_message(message.chat.id, f"Ваше имя: {user_data['name']}\nТеперь укажите ваш никнейм "
                                      f"в Telegram или номер телефона. Пожалуйста, проверьте, "
                                      f"чтобы это был рабочий контакт, и мы могли связаться с вами!"
                     )
    bot.register_next_step_handler(message, ask_brand)

def ask_brand(message):
    user_data['contact'] = message.text
    bot.send_message(message.chat.id, f"Ваш контакт: {user_data['contact']}\nРасскажите о своем "
                                      f"бренде/продукте/канале. Можно также поделиться "
                                      f"ссылкой на соцсети или сайт."
                     )
    bot.register_next_step_handler(message, ask_request)

def ask_request(message):
    user_data['brand_info'] = message.text
    bot.send_message(message.chat.id, f"Информация о бренде: {user_data['brand_info']}\nКратко расскажите "
                                      f"про свой запрос и задачу, с которой мы можем помочь."
                     )
    bot.register_next_step_handler(message, complete_request)

def complete_request(message):
    user_data['request'] = message.text
    complete_dict = {
        "Имя": user_data['name'],
        "Контакт": user_data['contact'],
        "Информация о бренде": user_data['brand_info'],
        "Запрос": user_data['request']
    }

    # Чтение существующих данных из файла leads.json
    if os.path.exists('leads.json'):
        with open('leads.json', 'r', encoding='utf-8') as leads_file:
            try:
                leads_data = json.load(leads_file)
                if not isinstance(leads_data, list):
                    leads_data = []  # Если это не список, создаем новый список
            except json.JSONDecodeError:
                leads_data = []  # Если файл пуст или поврежден, создаем пустой список
    else:
        leads_data = []  # Если файл не существует, создаем пустой список

    # Добавление новых данных в список
    leads_data.append(complete_dict)

    # Запись данных в файл
    with open('leads.json', 'w', encoding='utf-8') as leads_file:
        json.dump(leads_data, leads_file, ensure_ascii=False, indent=4)

    summary = (f"Спасибо за предоставленную информацию!\n\n"
               f"Имя: {user_data['name']}\n"
               f"Контакт: {user_data['contact']}\n"
               f"Информация о бренде: {user_data['brand_info']}\n"
               f"Запрос: {user_data['request']}")
    bot.send_message(message.chat.id, summary)

    # Отправка информации в личные сообщения администратору
    bot.send_message(ADMIN_CHAT_ID, f"Новая заявка от пользователя:\n\n{summary}")