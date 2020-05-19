import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup
from telebot.types import Message

TOKEN = '1218580832:AAGPlyC3ByIWHJe-N2Ot75s38ShgIP1E4t0'
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
first_button = types.KeyboardButton('Узнать расписание на сегодня')
second_button = types.KeyboardButton('Узнать расписание на конкретный день')
markup.add(first_button, second_button)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, text=f'<b>Привет, {message.from_user.first_name}</b>\nЗдесь ты можешь узнать расписание.',
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def messages(message: Message):
    days_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    ponedelnik = types.KeyboardButton('Понедельник')
    vtornik = types.KeyboardButton('Вторник')
    sreda = types.KeyboardButton('Среда')
    chetverg = types.KeyboardButton('Четверг')
    pyatnica = types.KeyboardButton('Пятница')
    days_keyboard.add(ponedelnik, vtornik, sreda, chetverg, pyatnica)
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu_button = types.KeyboardButton('Вернуться в меню')
    menu_keyboard.add(menu_button)
    if 'Узнать расписание на сегодня' in message.text:
        bot.send_message(message.chat.id, text='<b>Выберите какой сегодня день недели</b>', parse_mode='html',
                         reply_markup=days_keyboard)
    elif 'Узнать расписание на конкретный день' in message.text:
        bot.send_message(message.chat.id, text='<b>Выберите день недели</b>', parse_mode='html',
                         reply_markup=days_keyboard)
    elif 'Понедельник' in message.text:
        bot.send_message(message.chat.id, text='''
        (9:40 - 11:10) Средства и методы управ. кач. (лек.), Тищенко Е.А.\n(11:30 - 13:00) Средства и методы управ. кач. (практ.), Тищенко\n(13:10 - 14:40) Базы данных (лаб.), Зацепин М.Н.	 
        ''', reply_markup=menu_keyboard)
    elif 'Вторник' in message.text:
        bot.send_message(message.chat.id, text='''
        (8:00 - 9:30) Теор. осн. электр. Литвинов С.А.\n(9:40 - 11:10) Архитектура компьютера (лаб.), Пономаренко Т.Н.\n(11:30-13:00) Теория вероят. и мат. статист. (практ.), Шаповалова И.В.\n(13:10 - 14:40) Физкультура 
        ''', reply_markup=menu_keyboard)
    elif 'Среда' in message.text:
        bot.send_message(message.chat.id, text="(8:00 - 9:30) Теор. осн. электр. Литвинов С.А.\n(9:40-11:10) Материаловедение (лек.) Кудашова Д.С.\n(11:30 - 13:00) Материаловедение (практ.) Кудашова Д.С."
                                                   "\n(13:10 - 14:40) Архитектура компьютера (лек.) Пономаренко Т.Н.", reply_markup=menu_keyboard)
    elif 'Четверг' in message.text:
        bot.send_message(message.chat.id, text='''(13:10 - 14:40) Методы и сред. изм., исп. и кон. (лек.)Тищенко Е.А.\n(15:00 - 16:30) Методы и сред. изм., исп. и кон. (практ.)Тищенко\n(16:40 - 18:10) Статистика (практ.) Бабенко А.И.''', reply_markup=menu_keyboard)
    elif 'Пятница' in message.text:
        bot.send_message(message.chat.id, text='''(13:10 - 14:40) Физкультура\n(15:00 - 16:30) Инновационная экономика (практ.) Щербина К.О.\n(16:40 - 18:10) Метрол, стандарт. и сертиф. (практ.) Cальникова А.А''', reply_markup=menu_keyboard)
    elif 'Вернуться в меню' in message.text:
        bot.send_message(message.chat.id, text='<b>Меню</b>', parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text='Я не понимаю')




bot.polling()