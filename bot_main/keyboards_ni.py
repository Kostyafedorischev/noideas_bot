from telebot import types

# Главное меню с inline-кнопками
def main_menu():
    markup = types.InlineKeyboardMarkup()
    btn_about = types.InlineKeyboardButton("О нас", callback_data='about')
    btn_cases = types.InlineKeyboardButton("Наши кейсы", callback_data='cases')
    btn_services = types.InlineKeyboardButton("Услуги", callback_data='services')
    btn_socials = types.InlineKeyboardButton("Соц сети и сайт", callback_data='socials')
    btn_contact = types.InlineKeyboardButton("Оставить заявку", callback_data='contact')
    markup.add(btn_about, btn_cases)
    markup.add(btn_services, btn_socials)
    markup.add(btn_contact)
    return markup

# Меню кейсов с inline-кнопками
def cases_menu():
    markup = types.InlineKeyboardMarkup()
    btn_case_1 = types.InlineKeyboardButton("Кейс «Большая коллегия»", url='https://example.com/case1')
    btn_case_2 = types.InlineKeyboardButton("Кейс «Аникон»", url='https://example.com/case2')
    btn_case_3 = types.InlineKeyboardButton("Кейс «Целеполагалка»", url='https://example.com/case3')
    btn_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    markup.add(btn_case_1)
    markup.add(btn_case_2)
    markup.add(btn_case_3)
    markup.add(btn_back)
    return markup

# Меню услуг с inline-кнопками
def services_menu():
    markup = types.InlineKeyboardMarkup()
    btn_design = types.InlineKeyboardButton("Дизайн", callback_data='design')
    btn_marketing = types.InlineKeyboardButton("Маркет", callback_data='marketing')
    btn_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    markup.add(btn_design)
    markup.add(btn_marketing)
    markup.add(btn_back)
    return markup

# Меню социальных сетей
def socials_menu():
    markup = types.InlineKeyboardMarkup()
    btn_telegram = types.InlineKeyboardButton("Телеграм-канал", url='https://t.me/noideas_agency')
    btn_vc = types.InlineKeyboardButton("VC", url='https://vc.ru/u/1221951-no-ideas-agency')
    btn_site = types.InlineKeyboardButton("Наш сайт", url='https://noideas-agency.ru')
    btn_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    markup.add(btn_telegram, btn_vc)
    markup.add(btn_site)
    markup.add(btn_back)
    return markup

# Обработчик для общего текстового раздела (например, "О нас" и т.п.)
def text_menu():
    markup = types.InlineKeyboardMarkup()
    btn_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    markup.add(btn_back)
    return markup