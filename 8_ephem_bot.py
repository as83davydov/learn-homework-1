"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_user(update, context): #функция показывает в каком созвездии планета без команды
    date_planet = '2121/03/05'
   
    if update.message.text == 'mars':
        planet = ephem.Mars(date_planet)        
    elif update.message.text == 'venus':
        planet = ephem.Venus(date_planet)
    elif update.message.text == 'jupiter':
        planet = ephem.Jupiter(date_planet)
    elif update.message.text == 'earth':
        planet = ephem.Earth(date_planet)      
    else:
      update.message.reply_text('что-то пошло не так')
      return

    const_planet = ephem.constellation(planet)
    update.message.reply_text(f'{date_planet} Планета {update.message.text.upper()} в созвездии {const_planet[-1]}')

  
def get_planet(update, context): #функция показывает в каком созвездии планета с командой /planet
    date_user = '2121/03/05' #input('Введите дату в формате год/месяц/день: ')

    if context.args[0] == 'mars':
        planetname = ephem.Mars(date_user)
    elif context.args[0] == 'venus':
        planetname = ephem.Venus(date_user)
    elif context.args[0] == 'jupiter':
        planetname = ephem.Jupiter(date_user)
    elif context.args[0] == 'earth':
        planetname = ephem.Earth(date_user)
    elif context.args[0] == 'moon':
        planetname = ephem.Moon(date_user)
    elif context.args[0] == 'sun':
        planetname = ephem.Sun(date_user)
    elif context.args[0] == 'uranus':
        planetname = ephem.Uranus(date_user)
    elif context.args[0] == 'pluto':
        planetname = ephem.Pluto(date_user)
    else:
        update.message.reply_text('ошибочка вышла')
        return

    constel_planet = ephem.constellation(planetname)
    update.message.reply_text(f'{date_user} Планета {context.args[0].upper()} в созвездии {constel_planet[-1]}')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()