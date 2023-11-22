import vk_api
from bs4 import BeautifulSoup
import requests
import re
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from datetime import datetime, timedelta

# Авторизация
vk_session = vk_api.VkApi(token= '') #ввести токен
group_id = #номер группы
longpoll = VkBotLongPoll(vk_session,group_id)
vk = vk_session.get_api()
# Создание клавиатуры с кнопками
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Создание шаблона для анонса', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Подсчёт порций,закупаемых продуктов,воды', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()  # Создание новой строки для кнопок
keyboard.add_button('Ссылка на офлайн карты', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Кнопка 4', color=VkKeyboardColor.NEGATIVE)

def send_message(peer_id, message):
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=get_random_id(),
    )
# функция для проверки даты регистрации аккаунта пользователя
def kick(from_id,peer_id,message):
    response = requests.get('https://vk.com/foaf.php?id=' + from_id)
    xml = response.text
    soup = BeautifulSoup(xml, 'lxml')
    created = soup.find('ya:created').get('dc:date')
    c_split = re.split('-|:|T', created)
    print(c_split)
    year = int(c_split[0])
    mouth = int(c_split[1])
    day = int(c_split[2])
    print(year)
    print(mouth)
    print(day)
    current_date = str(datetime.now())
    print(current_date)
    current_date_splt = re.split('-|:| ', current_date)
    year_cur = int(current_date_splt[0])
    mouth_cur = int(current_date_splt[1])
    day_cur = int(current_date_splt[2])
    print(year_cur)
    print(mouth_cur)
    print(day_cur)
    print(peer_id)
    print(peer_id)
    if year_cur-year == 0:
        if mouth_cur-mouth == 0:
            if day_cur-day < 7:
                if peer_id != int(from_id):
                    vk_session.method('messages.removeChatUser', {'user_id': from_id, 'chat_id': peer_id - 2000000000})
                else:
                    print('ровняется')
            else:
                print("Всё ок")
        else:
            print("Всё ок")
    else:
        print("Всё ок")


# основная функция бота


# запуск бота
#
#
def podshet(user_id):
    send_message(user_id, "Привет! Я бот для расчёта пропитания.")
    send_message(user_id, "Отправте сейчас любое сообщение чтобы продолжить.")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            send_message(user_id, "Напиши количество людей(с уточнением мужчина-женщина):")
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    people = event.message.text
                    send_message(user_id, "Количетсво людей записано.")

                    send_message(user_id, "Напиши из этого количества количество всеядных и веганов:")

                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            veg_vsead = event.message.text
                            send_message(user_id, "Количество записано.")

                            send_message(user_id, "Напиши количество дней")

                            for event in longpoll.listen():
                                if event.type == VkBotEventType.MESSAGE_NEW:
                                    days = event.message.text
                                    send_message(user_id, "Количество дней записано.")

                                    send_message(user_id, "Напиши присутствие родников и других способов пополнения воды(организаторы, если вы сами будете пополнять воду, напишите это)")

                                    for event in longpoll.listen():
                                        if event.type == VkBotEventType.MESSAGE_NEW:
                                            voda = event.message.text
                                            send_message(user_id, "Пополнение воды записано.")

                                            send_message(user_id, f"👫 Количество людей: {people}\n" \
                                                                  f"🍀🐔 Количество вегатерианцов и всеядных: {veg_vsead}\n" \
                                                                  f"⏳ Количество дней: {days}\n" \
                                                                  f"💧 Пополнение воды: {voda}")
                                            return


def start_dialog(user_id):
    send_message(user_id, "Привет! Я бот для создания шаблона анонса.")
    send_message(user_id, "Отправте сейчас любое сообщение чтобы продолжить.")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
                send_message(user_id, "Напиши место назначение:")
                for event in longpoll.listen():
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        dest = event.message.text
                        send_message(user_id, "Место назначение записан.")

                        send_message(user_id, "Напиши продолжительность похода:")

                        for event in longpoll.listen():
                            if event.type == VkBotEventType.MESSAGE_NEW:
                                duration = event.message.text
                                send_message(user_id, "Дата проведения записана.")

                                send_message(user_id, "Напиши сложность маршрута" )

                                for event in longpoll.listen():
                                    if event.type == VkBotEventType.MESSAGE_NEW:
                                        difficulty = event.message.text
                                        send_message(user_id, "Сложность маршрута записана.")

                                        send_message(user_id, "Напиши на чём вы поедете")

                                        for event in longpoll.listen():
                                            if event.type == VkBotEventType.MESSAGE_NEW:
                                                transportation = event.message.text
                                                send_message(user_id, "Транспорт записан.")

                                                send_message(user_id, "Напиши стоимость проезда туда и обратно")

                                                for event in longpoll.listen():
                                                    if event.type == VkBotEventType.MESSAGE_NEW:
                                                        cost = event.message.text
                                                        send_message(user_id, "Стоимость записана.")

                                                        send_message(user_id, "Напиши место и время сбора")
                                                        for event in longpoll.listen():
                                                            if event.type == VkBotEventType.MESSAGE_NEW:
                                                                gathering_time_location = event.message.text
                                                                send_message(user_id, "Место и время сбора записаны.")

                                                                send_message(user_id, "Напиши гугл форму для регистрации и для полной информации")
                                                                for event in longpoll.listen():
                                                                    if event.type == VkBotEventType.MESSAGE_NEW:
                                                                        google_form_link = event.message.text
                                                                        send_message(user_id,
                                                                                     "гугл форма записана.")

                                                                        send_message(user_id, f"🌍 Место назначения: {dest}\n" \
                                                                                                                               f"⏳ Продолжительность: {duration}\n" \
                                                                                                                               f"📈 Сложность: {difficulty}\n" \
                                                                                                                               f"🚗 Транспорт: {transportation}\n" \
                                                                                                                               f"💰 Стоимость проезда туда и обратно: {cost}\n" \
                                                                                                                               f"🕒 Место и время сбора: {gathering_time_location}\n" \
                                                                                                                               f"📋 Более подробная информация и регистрация: {google_form_link}")
                                                                        return
# Основной цикл обработки событий
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        from_id = str(event.message.from_id)  # id пользователя, который отправил сообщение
        peer_id = event.message.peer_id  # peer_id беседы или ЛС, откуда пришло сообщение
        message = event.message.text
        print(from_id)
        print(peer_id)
        print(message)
        kick(from_id, peer_id, message)
        if event.message.text.lower() == 'привет' and event.from_user:
            vk.messages.send(peer_id=peer_id,message=message,random_id=get_random_id(), keyboard=keyboard.get_keyboard())
        elif event.message.text.lower() == 'создание шаблона для анонса' and event.from_user:
            start_dialog(from_id)
        elif event.message.text.lower() == 'подсчёт порций,закупаемых продуктов,воды' and event.from_user:
            podshet(from_id)
        elif event.message.text.lower() == 'ссылка на офлайн карты' and event.from_user:
            vk.messages.send(from_id=from_id,peer_id=peer_id,message="Maps.me",random_id=get_random_id(),keyboard=keyboard.get_keyboard())
        elif event.message.text.lower() == 'кнопка 4' and event.from_user:
            vk.messages.send(from_id=from_id,peer_id=peer_id,message=message,random_id=get_random_id(),keyboard=keyboard.get_keyboard())