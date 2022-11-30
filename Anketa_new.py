#!/usr/bin/env python3
import telebot
from telebot import types
import fast_bitrix24
import base64
import asyncio
import time





API_TOKEN = 'API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}



class User:
    def __init__(self, name):
        self.name = None
        self.age = None
        self.birthdate = None
        self.sex = None
        self.city = None
        self.phone = None
        self.email = None
        self.social = None
        self.language = None
        self.language2 = None
        self.relationship = None
        self.kids = None
        self.hobby = []
        self.trips = None
        self.citizenship = None
        self.passport = None
        self.person = None
        self.race = None
        self.skin = None
        self.face = None
        self.nose = None
        self.eyes = None
        self.eyecolor = None
        self.lips = None
        self.hair = None
        self.hairstyle = None
        self.hairlength = None
        self.height = None
        self.height2 = None
        self.shoes = None
        self.clothes = None
        self.constitution = None
        self.waist = None
        self.hips = None
        self.bust = None
        self.breast = None
        self.cosmetic = None
        self.cosmetology = None
        self.tattoo = None
        self.stomato = None
        self.speech = None
        self.facehair = None
        self.bodyhair = None
        self.status = None
        self.education = None
        self.prof = []
        self.achievments = None
        self.skills = None
        self.qualities = []
        self.character = []
        self.type = []
        self.orientation = None
        self.under = None
        self.art = []


numbers = ('1','2','3','4','5','6','7','8','9','0')

languagespisok = {'Английский базовый': '1358', 'Английский продвинутый': '1360', 'Немецкий базовый': '1362', 'Немецкий продвинутый': '1364', 'Другие языки': '1366'}
citizenshipspisok = {'Гражданин РФ': '400', 'Нерезидент РФ': '1356', 'СНГ': '402'}
tripsspisok = {'Да, на короткий срок': '710', 'Да, на длительный срок': '710', 'Нет': '712'}
educationspisok = {'Среднее': '1458', 'Специальное': '1462', 'Неоконченное высшее': '1456', 'Высшее': '1454'}
statusspisok = {'Трудоустроен': '1464', 'Безработный': '1466', 'Студент': '1468', 'Пенсионер': '1470', 'Самозанятый': '3298'}
facehairspisok = {'Отсутствует': '3118', 'Усы': '1308', 'Борода': '1310', 'Щетина': '1312', 'Американская бородка': '1314', 'Монобровь': '1316'}
stomatospisok = {'Без особенностей': '1288', 'Голливудская улыбка': '1296', 'Брекеты': '4696', 'Редкие зубы': '1290', 'Кривые зубы': '1292', 'Отсутствие видимых зубов': '1294'}
speechspisok = {'Отчётливая': '1298', 'Искаженность': '1300', 'Картавость': '1302', 'Шепелявость': '1304', 'Акцент': '1306'}
tattoospisok = {'Без татуировок': '390', 'Невидимая (под одеждой)': '388', 'На видном месте': '1324', 'Многочисленные татуировки': '1326'}
cosmetologyspisok = {'Естественная': '1328', 'Импланты': '1330', 'Ботокс': '1332'}
cosmeticspisok = {'Отсутствуют': '1334', 'Татуаж': '1336', 'Нарощенные ресницы': '1338', 'Пирсинг': '1340', 'Другое': '3242'}
breastspisok = {'нет':'680', '0':'680', '1':'680', '2':'682', '3':'684', '4':'686','5':'686','6':'686','7':'686','8':'686'}
clothesspisok = {'XS 40-42': '670', 'S 44': '672', 'M 46':'674', 'L 48': '676', 'XL 50-52':'678', 'XXL 54-56': '1174', 'XXXL 56-58': '1176'}
hairstylespisok = {'Наголо': '1202', 'Коротко': '1204', 'Средняя длина': '1206', 'Длинные': '1208', 'Редкие/С плешью': '1210'}
hairspisok = {'Блонд': '660', 'Темно-русый': '662', 'Брюнет/ка': '664', 'Рыжий': '666', 'Светло-русый': '668', 'Шатен/ка': '1212', 'Седой': '1214', 'Седой, но крашенный': '1216', 'Креативное окрашивание': '1216'}
eyecolorspisok = {'Серый': '646', 'Зеленый': '648', 'Синий': '650', 'Голубой': '650', 'Янтарный': '1248', 'Ореховый': '652', 'Карий': '652', 'Черный':'1250', 'Смешанный': '1250'}
eyesspisok = {'Миндалевидные': '1236', 'Восточный разрез':'1238', 'Круглые': '1240', 'Выпуклые глаза': '1242', 'Близко посаженные': '1244', 'Широко посаженные': '1246'}
nosespisok = {'Прямой': '1264', 'Греческий': '1268', 'Римский': '1270', 'Курносый': '1272', 'Картошкой': '1274', 'Ястрибиный': '1276', 'С горбинкой': '1266'}
facespisok = {'Круглое': '1194', 'Овальное': '1192', 'Удлиненное': '1196', 'Треугольное': '1200', 'Квадратное': '1198'}
racespisok = {'Американоидная': '1344', 'Европеоидная': '1342', 'Монголоидная': '1346', 'Негроидная': '1348', 'Эфиопская': '1350', 'Метис': '1352', 'Мулат': '1354'}
hobbyspisok = {'Танцы' : '1398', 'Вокал': '1400', 'Спорт': '1402', 'Массовка': '3158', 'Блогер': '3162', 'Домоводство': '3260', 'Компьютерные игры': '3258', 'Кулинария': '3256', 'Живопись': '3254', 'Фотография': '3252', 'Рукоделие': '3250', 'Стилист': '3164', 'Визажист': '3164', 'ДАЛЕЕ': 'ДАЛЕЕ'}
profspisok = {'Модель': '356', 'Актер': '364', 'Актер Массовых сцен': '364', 'Хостес': '362',
              'Актер дубляжа': '5845', 'Арт-директор': '386', 'Артист цирка': '1432', 'Бариста': '500', 'Бармен': '370', 'Блогер': '360',
              'Букер/Рекрут': '384', 'Визажист': '1422', 'Водитель': '1436', 'Диджей': '372', 'Звукорежиссёр': '1424', 'HR-менеджер': '570',
              'Каскадёр': '1434', 'Кастинг директор': '1426', 'Онлайн ведущий': '358', 'Организатор Event мероприятий': '1418', 'Официант': '1430', 'Певец': '366',
              'Переводчик': '376', 'Промоутер': '380', 'Скаут': '382', 'Стилист': '1420', 'Танцор': '368', 'Телохранитель': '374', 'Фотограф': '1428', 'ДАЛЕЕ': 'ДАЛЕЕ'}
artspisok = {'Аранжировщик': '1406', 'Исполнитель': '1408', 'Комик': '1414', 'Композитор': '1404', 'Писатель/Поэт': '1410', 'Стэндапер': '1412', 'ДАЛЕЕ': 'ДАЛЕЕ'}
qualitiesspisok = {'Дружелюбность': '1370', 'Коммуникабельность': '1368', 'Активность': '1374', 'Ответственность': '1372', 'Пунктуальность': '1376', 'ДАЛЕЕ': 'ДАЛЕЕ'}
characterspisok = {'Агрессивный': '1378', 'Импульсивный': '1380', 'Замкнутый': '1382', 'Нерешительный': '1384', 'Вспыльчивый': '1386', 'Безэмоциональный': '1388',
                   'Жизнерадостный': '3126', 'Отзывчивый': '3128', 'Решительный': '3130', 'Спокойный': '3132', 'ДАЛЕЕ': 'ДАЛЕЕ'}
typespisok = {'Веселый': '1392', 'Драматический': '1390', 'Комерческий': '1394', 'Представительный': '1396', 'ДАЛЕЕ': 'ДАЛЕЕ'}
# Handle '/start' and '/help'



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Добро пожаловать"
""")
    bot.register_next_step_handler(msg, process_name_step)
    bot.send_message(message.chat.id, 'Начнём. Введите ваше имя')


#Ввод имени и переход на город
def process_name_step(message):
    try:
        global numbers
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user.name = name
        for i in name:
            if i in numbers:
                msg = bot.reply_to(message, 'Вы ввели недопустимые символы. Попробуйте еще раз')
                bot.register_next_step_handler(msg, process_name_step)
                return
        user_dict[chat_id] = user
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Калининград', 'Москва')
        msg = bot.reply_to(message, 'Укажите ваш город', reply_markup=markup)
        bot.register_next_step_handler(msg, process_city_step)
    except Exception as e:
        bot.reply_to(message, 'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 1')




#Город и переход на возраст
def process_city_step(message):
    try:
        chat_id = message.chat.id
        city = message.text
        user = user_dict[chat_id]
        if (city == 'Калининград') or (city == 'Москва'):
            if city == 'Калининград':
                user.city = '566'
            elif city == 'Москва':
                user.city == '564'
        else:
            msg = bot.reply_to(message, 'Выберите вариант из предложенных')
            bot.register_next_step_handler(msg, process_city_step)
            return
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Ваш возраст?', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 2')


#Возраст и переход на номер телефона
def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Возраст должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_age_step)
            return
        if 15 >= int(age) or int(age) >= 100:
            msg = bot.reply_to(message, 'Вы ввели недопустимый возраст')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        msg = bot.reply_to(message, 'Введите вашу дату рождения в формате "01.12.1990"')
        bot.register_next_step_handler(msg, process_birthdate_step)
    except Exception as e:
        bot.reply_to(message, 'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 3')


def process_birthdate_step(message):
    try:
        chat_id = message.chat.id
        birthdate = message.text
        user = user_dict[chat_id]
        if '.' not in birthdate:
            msg = bot.reply_to(message, 'Вы ввели некорректную дату. Введите вашу дату рождения в формате "01.12.1990"')
            bot.register_next_step_handler(msg, process_birthdate_step)
            return
        user.birthdate = birthdate
        msg = bot.reply_to(message, 'Введите вашe ссылку на социальные сети, или оставьте прочерк "-"')
        bot.register_next_step_handler(msg, process_social_step)
    except Exception as e:
        bot.reply_to(message, 'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 4')



def process_social_step(message):
    try:
        chat_id = message.chat.id
        social = message.text
        user = user_dict[chat_id]
        user.social = social
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for i in languagespisok:
            markup.add(i)
        msg = bot.reply_to(message, 'Укажите, каким языком вы владеете?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_language_step)
    except:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 5')


def process_language_step(message):
    try:
        chat_id = message.chat.id
        language = message.text
        user = user_dict[chat_id]
        if language in languagespisok:
            user.language = languagespisok[language]
            msg = bot.reply_to(message, 'Укажите через запятую, какими еще языками вы владеете, и уровень владения ими', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_language2_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 5')


def process_language2_step(message):
    try:
        chat_id = message.chat.id
        language = message.text
        user = user_dict[chat_id]
        user.language2 = language
        msg = bot.reply_to(message, 'Введите ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 6')


def process_phone_step(message):
    try:
        chat_id = message.chat.id
        phone = message.text
        if phone[0] == '+' and phone[1] == '7':
            phonenumber = phone[1:]
            if not phonenumber.isdigit() or len(phonenumber) != 11:
                msg = bot.reply_to(message, 'Введите корректный номер. *Корректный номер начинается с +7 и 10 цифр после*', parse_mode= "Markdown")
                bot.register_next_step_handler(msg, process_phone_step)
                print(phonenumber, len(phonenumber))
                return
        else:
            msg = bot.reply_to(message, 'Вы ввели некорректный номер. *Начните с +7*', parse_mode= "Markdown")
            bot.register_next_step_handler(msg, process_phone_step)
            return
        user = user_dict[chat_id]
        user.phone = phone
        msg = bot.reply_to(message, 'Укажите ваш email')
        bot.register_next_step_handler(msg, process_email_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 7')



def process_email_step(message):
    try:
        chat_id = message.chat.id
        email = message.text
        if '@' not in email:
            msg = bot.reply_to(message, 'Введите корректный email')
            bot.register_next_step_handler(msg, process_email_step)
            return
        if '.' not in email:
            msg = bot.reply_to(message, 'Введите корректный email')
            bot.register_next_step_handler(msg, process_email_step)
            return
        user = user_dict[chat_id]
        user.email = email
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Мужчина', 'Женщина')
        msg = bot.reply_to(message, 'Укажите ваш пол', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 8')



def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == 'Мужчина') or (sex == 'Женщина'):
            if sex == 'Мужчина':
                user.sex = '552'
            elif sex == 'Женщина':
                user.sex = '554'
        else:
            msg = bot.reply_to(message, 'Введите корректный пол. Выбрать его можете с помощью кнопок')
            bot.register_next_step_handler(msg, process_email_step)
            return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Женат/Замужем', 'Живем вместе', 'Встречаюсь', 'В разводе', 'Нет')
        msg = bot.reply_to(message, 'Ваше семейное положение', reply_markup=markup)
        bot.register_next_step_handler(msg, process_relationship_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 9')


def process_relationship_step(message):
    try:
        chat_id = message.chat.id
        relationship = message.text
        user = user_dict[chat_id]
        if relationship == 'Женат/Замужем' or relationship == 'Живем вместе' or relationship == 'Встречаюсь' or relationship == 'В разводе' or relationship == 'нет':
            if relationship == 'Женат/Замужем':
                user.relationship = 698
            else:
                user.relationship = 700
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да', 'Нет')
            msg = bot.reply_to(message, 'Есть ли у вас дети?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_kids_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_relationship_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 10')


def process_kids_step(message):
    try:
        chat_id = message.chat.id
        kids = message.text
        user = user_dict[chat_id]
        if kids == 'Да':
            user.kids = 706
        elif kids == 'Нет':
            user.kids == 708
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_kids_step)
            return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Гражданин РФ', 'Нерезидент РФ', 'СНГ')
        msg = bot.reply_to(message, 'Гражданство', reply_markup=markup)
        bot.register_next_step_handler(msg, process_citizenship_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 11')


def process_citizenship_step(message):
    try:
        chat_id = message.chat.id
        citizenship = message.text
        user = user_dict[chat_id]
        if citizenship in citizenshipspisok:
            user.citizenship = citizenshipspisok[citizenship]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Действующий', 'Недействующий', 'Не имеется')
            msg = bot.reply_to(message, 'Наличие загран. паспорта', reply_markup=markup)
            bot.register_next_step_handler(msg, process_passport_step)
            print(user.citizenship)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_citizenship_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 12')


def process_passport_step(message):
    try:
        chat_id = message.chat.id
        passport = message.text
        user = user_dict[chat_id]
        if passport == 'Действующий' or passport == 'Недействующий' or passport == 'Не имеется':
            if passport == 'Действующий':
                user.passport = 392
            else:
                user.passport = 394
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Славянский', 'Европейский', 'Монгольский', 'Афро-американский')
            msg = bot.reply_to(message, 'Тип внешности', reply_markup=markup)
            bot.register_next_step_handler(msg, process_person_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_passport_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 13')


def process_person_step(message):
    try:
        chat_id = message.chat.id
        person = message.text
        user = user_dict[chat_id]
        if person == 'Славянский' or person == 'Европейский' or person == 'Монгольский' or person == 'Афро-американский':
            if person == 'Славянский':
                user.person = 638
            elif person == 'Европейский':
                user.person = 640
            elif person == 'Монгольский':
                user.person = 642
            elif person == 'Афро-американский':
                user.person = 644
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Американоидная', 'Европеоидная', 'Монголоидная', 'Негроидная', 'Эфиопская', 'Метис', 'Мулат')
            msg = bot.reply_to(message, 'Расовая принадлежность', reply_markup=markup)
            bot.register_next_step_handler(msg, process_race_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_person_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 14')


def process_race_step(message):
    try:
        chat_id = message.chat.id
        race = message.text
        user = user_dict[chat_id]
        if race in racespisok:
            user.race = racespisok[race]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Белый', 'Смуглый', 'Загорелый', 'Черный')
            msg = bot.reply_to(message, 'Цвет кожи', reply_markup=markup)
            bot.register_next_step_handler(msg, process_skin_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_race_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 15')


def process_skin_step(message):
    try:
        chat_id = message.chat.id
        skin = message.text
        user = user_dict[chat_id]
        if skin == 'Белый' or skin == 'Смуглый' or skin == 'Загорелый' or skin == 'Черный':
            if skin == 'Белый':
                user.skin = '654'
            elif skin == 'Смуглый':
                user.skin = '656'
            elif skin == 'Загорелый':
                user.skin = '658'
            elif skin == 'Черный':
                user.skin = '1190'
            print(user.skin)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Круглое', 'Овальное', 'Удлиненное', 'Треугольное', 'Квадратное')
            msg = bot.reply_to(message, 'Форма лица', reply_markup=markup)
            bot.register_next_step_handler(msg, process_face_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_skin_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 16')



def process_face_step(message):
    try:
        chat_id = message.chat.id
        face = message.text
        user = user_dict[chat_id]
        if face in facespisok:
            user.face = facespisok[face]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Прямой', 'Греческий', 'Римский', 'Курносый', 'Картошкой', 'Ястрибиный', 'С горбинкой')
            msg = bot.reply_to(message, 'Форма Носа', reply_markup=markup)
            bot.register_next_step_handler(msg, process_nose_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_face_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 17')



def process_nose_step(message):
    try:
        chat_id = message.chat.id
        nose = message.text
        user = user_dict[chat_id]
        if nose in nosespisok:
            user.nose = nosespisok[nose]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Миндалевидные', 'Восточный разрез', 'Круглые', 'Выпуклые глаза', 'Близко посаженные', 'Широко посаженные')
            msg = bot.reply_to(message, 'Форма Глаз', reply_markup=markup)
            bot.register_next_step_handler(msg, process_eyes_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_nose_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 18')



def process_eyes_step(message):
    try:
        chat_id = message.chat.id
        eyes = message.text
        user = user_dict[chat_id]
        if eyes in eyesspisok:
            user.eyes = eyesspisok[eyes]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Серый', 'Зеленый', 'Синий', 'Голубой', 'Янтарный', 'Ореховый', 'Карий', 'Черный', 'Смешанный')
            msg = bot.reply_to(message, 'Цвет Глаз', reply_markup=markup)
            bot.register_next_step_handler(msg, process_eyecolor_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_eyes_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 19')



def process_eyecolor_step(message):
    try:
        chat_id = message.chat.id
        eyecolor = message.text
        user = user_dict[chat_id]
        if eyecolor in eyecolorspisok:
            user.eyecolor = eyecolorspisok[eyecolor]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Естественные', 'Тонкие', 'Пухлые', 'Неровные')
            msg = bot.reply_to(message, 'Губы', reply_markup=markup)
            bot.register_next_step_handler(msg, process_lips_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_eyecolor_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 20')



def process_lips_step(message):
    try:
        chat_id = message.chat.id
        lips = message.text
        user = user_dict[chat_id]
        if lips == 'Естественные' or lips == 'Тонкие' or lips == 'Пухлые' or lips == 'Неровные':
            if lips == 'Естественные':
                user.lips = 3214
            elif lips == 'Тонкие':
                user.lips = 3216
            elif lips == 'Пухлые':
                user.lips = 3218
            elif lips == 'Неровные':
                user.lips = 3220
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Блонд', 'Темно-русый', 'Брюнет/ка', 'Рыжий', 'Светло-русый', 'Шатен/ка', 'Седой', 'Седой, но крашенный', 'Креативное окрашивание')
            msg = bot.reply_to(message, 'Цвет Волос', reply_markup=markup)
            bot.register_next_step_handler(msg, process_hair_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_lips_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 21')



def process_hair_step(message):
    try:
        chat_id = message.chat.id
        hair = message.text
        user = user_dict[chat_id]
        if hair in hairspisok:
            user.hair = hairspisok[hair]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Наголо', 'Коротко', 'Средняя длина', 'Длинные', 'Редкие/С плешью')
            msg = bot.reply_to(message, 'Стрижка', reply_markup=markup)
            bot.register_next_step_handler(msg, process_hairstyle_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_hair_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 22')



def process_hairstyle_step(message):
    try:
        chat_id = message.chat.id
        hairstyle = message.text
        user = user_dict[chat_id]
        if hairstyle in hairstylespisok:
            user.hairstyle = hairstylespisok[hairstyle]
            msg = bot.reply_to(message, 'Длина волос', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_hairlength_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_hairstyle_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 23')





def process_hairlength_step(message):
    try:
        chat_id = message.chat.id
        hairlength = message.text
        user = user_dict[chat_id]
        if not hairlength.isdigit():
            msg = bot.reply_to(message, 'Длина волос должна быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_hairlength_step)
            return
        user.hairlength = hairlength
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Низкий (до 160 см)', 'Средний (до 180 см)', 'Высокий (Свыше 180см)')
        msg = bot.reply_to(message, 'Рост', reply_markup=markup)
        bot.register_next_step_handler(msg, process_height_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 24')



def process_height_step(message):
    try:
        chat_id = message.chat.id
        height = message.text
        user = user_dict[chat_id]
        if height == 'Низкий (до 160 см)' or height == 'Средний (до 180 см)' or height == 'Высокий (Свыше 180см)':
            if height == 'Низкий (до 160 см)':
                user.height = '1156'
            elif height == 'Средний (до 180 см)':
                user.height = '1158'
            elif height == 'Высокий (Свыше 180см)':
                user.height = '1160'
            msg = bot.reply_to(message, 'Ваш рост, см', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_height2_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_height_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 25')



def process_height2_step(message):
    try:
        chat_id = message.chat.id
        height2 = message.text
        user = user_dict[chat_id]
        if not height2.isdigit():
            msg = bot.reply_to(message, 'Рост должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_height2_step)
            return
        user.height2 = height2
        msg = bot.reply_to(message, 'Размер обуви')
        bot.register_next_step_handler(msg, process_shoes_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 26')


def process_shoes_step(message):
    try:
        chat_id = message.chat.id
        shoes = message.text
        user = user_dict[chat_id]
        if not shoes.isdigit():
            msg = bot.reply_to(message, 'Размер обуви должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_shoes_step)
            return
        user.shoes = shoes
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('XS 40-42', 'S 44', 'M 46', 'L 48', 'XL 50-52', 'XXL 54-56', 'XXXL 56-58')
        msg = bot.reply_to(message, 'Размер одежды', reply_markup=markup)
        bot.register_next_step_handler(msg, process_clothes_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 27')



def process_clothes_step(message):
    try:
        chat_id = message.chat.id
        clothes = message.text
        user = user_dict[chat_id]
        if clothes in clothesspisok:
            user.clothes = clothesspisok[clothes]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Спортивный', 'Статный', 'Сутулый', 'Стройный', 'Дистрофия', 'Полное')
            msg = bot.reply_to(message, 'Телосложение', reply_markup=markup)
            bot.register_next_step_handler(msg, process_constitution_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_clothes_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 28')



def process_constitution_step(message):
    try:
        chat_id = message.chat.id
        constitution = message.text
        user = user_dict[chat_id]
        if constitution == 'Статный' or constitution == 'Сутулый' or constitution == 'Стройный' or constitution == 'Дистрофия' or constitution == 'Полное' or constitution == 'Спортивный':
            if constitution == 'Статный':
                user.constitution = '1164'
            elif constitution == 'Сутулый':
                user.constitution = '1166'
            elif constitution == 'Стройный':
                user.constitution = '1168'
            elif constitution == 'Дистрофия':
                user.constitution = '1170'
            elif constitution == 'Полное':
                user.constitution = '1172'
            elif constitution == 'Спортивный':
                user.constitution = '1162'
            msg = bot.reply_to(message, 'Объем Талии, см', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(msg, process_waist_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_constitution_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 29')



def process_waist_step(message):
    try:
        chat_id = message.chat.id
        waist = message.text
        user = user_dict[chat_id]
        if not waist.isdigit():
            msg = bot.reply_to(message, 'Объем талии должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_waist_step)
            return
        user.waist = waist
        msg = bot.reply_to(message, 'Объем бедер, см')
        bot.register_next_step_handler(msg, process_hips_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 30')



def process_hips_step(message):
    try:
        chat_id = message.chat.id
        hips = message.text
        user = user_dict[chat_id]
        if not hips.isdigit():
            msg = bot.reply_to(message, 'Объем бёдер должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_hips_step)
            return
        user.hips = hips
        msg = bot.reply_to(message, 'Бюст, см')
        bot.register_next_step_handler(msg, process_bust_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 31')



def process_bust_step(message):
    try:
        chat_id = message.chat.id
        bust = message.text
        user = user_dict[chat_id]
        if not bust.isdigit():
            msg = bot.reply_to(message, 'Объем бюста должен быть цифрой. Попробуйте еще раз')
            bot.register_next_step_handler(msg, process_bust_step)
            return
        user.bust = bust
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('нет', '0', '1', '2', '3', '4','5','6','7','8')
        msg = bot.reply_to(message, 'Размер груди', reply_markup=markup)
        bot.register_next_step_handler(msg, process_breast_step)
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 32')



def process_breast_step(message):
    try:
        chat_id = message.chat.id
        breast = message.text
        user = user_dict[chat_id]
        if breast in breastspisok:
            user.breast = breastspisok[breast]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Отсутствуют', 'Татуаж', 'Нарощенные ресницы', 'Пирсинг', 'Другое')
            msg = bot.reply_to(message, 'Косметические особенности', reply_markup=markup)
            bot.register_next_step_handler(msg, process_cosmetic_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_breast_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 33')



def process_cosmetic_step(message):
    try:
        chat_id = message.chat.id
        cosmetic = message.text
        user = user_dict[chat_id]
        if cosmetic in cosmeticspisok:
            user.cosmetic = cosmeticspisok[cosmetic]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Естественная', 'Импланты', 'Ботокс')
            msg = bot.reply_to(message, 'Косметологические особенности', reply_markup=markup)
            bot.register_next_step_handler(msg, process_cosmetology_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_cosmetic_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 34')




def process_cosmetology_step(message):
    try:
        chat_id = message.chat.id
        cosmetology = message.text
        user = user_dict[chat_id]
        if cosmetology in cosmetologyspisok:
            user.cosmetology = cosmetologyspisok[cosmetology]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Без татуировок', 'Невидимая (под одеждой)', 'На видном месте', 'Многочисленные татуировки')
            msg = bot.reply_to(message, 'Наличие татуировок', reply_markup=markup)
            bot.register_next_step_handler(msg, process_tattoo_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_cosmetology_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 35')



def process_tattoo_step(message):
    try:
        chat_id = message.chat.id
        tattoo = message.text
        user = user_dict[chat_id]
        if tattoo in tattoospisok:
            user.tattoo = tattoospisok[tattoo]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Без особенностей', 'Голливудская улыбка', 'Брекеты', 'Редкие зубы', 'Кривые зубы', 'Отсутствие видимых зубов')
            msg = bot.reply_to(message, 'Стоматологические особенности', reply_markup=markup)
            bot.register_next_step_handler(msg, process_stomato_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_tattoo_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 36')



def process_stomato_step(message):
    try:
        chat_id = message.chat.id
        stomato = message.text
        user = user_dict[chat_id]
        if stomato in stomatospisok:
            user.stomato = stomatospisok[stomato]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Отчётливая', 'Искаженность', 'Картавость', 'Шепелявость', 'Акцент')
            msg = bot.reply_to(message, 'Речевые особенности', reply_markup=markup)
            bot.register_next_step_handler(msg, process_speech_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_stomato_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 37')


def process_speech_step(message):
    try:
        chat_id = message.chat.id
        speech = message.text
        user = user_dict[chat_id]
        if speech in speechspisok:
            user.speech = speechspisok[speech]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Отсутствует', 'Усы', 'Борода', 'Щетина', 'Американская бородка', 'Монобровь')
            msg = bot.reply_to(message, 'Растительность на лице', reply_markup=markup)
            bot.register_next_step_handler(msg, process_facehair_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_speech_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 38')


def process_facehair_step(message):
    try:
        chat_id = message.chat.id
        facehair = message.text
        user = user_dict[chat_id]
        if facehair in facehairspisok:
            user.facehair = facehairspisok[facehair]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Отсутствует', 'Немного', 'Много')
            msg = bot.reply_to(message, 'Растительность на груди', reply_markup=markup)
            bot.register_next_step_handler(msg, process_bodyhair_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_facehair_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 39')



def process_bodyhair_step(message):
    try:
        chat_id = message.chat.id
        bodyhair = message.text
        user = user_dict[chat_id]
        if bodyhair == 'Отсутствует' or bodyhair == 'Немного' or bodyhair == 'Много':
            if bodyhair == 'Отсутствует':
                user.bodyhair = '1318'
            elif bodyhair == 'Немного':
                user.bodyhair = '1320'
            elif bodyhair == 'Много':
                user.bodyhair = '1322'
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Трудоустроен', 'Безработный', 'Студент','Пенсионер','Самозанятый')
            msg = bot.reply_to(message, 'Социальный статус', reply_markup=markup)
            bot.register_next_step_handler(msg, process_status_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_bodyhair_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 40')



def process_status_step(message):
    try:
        chat_id = message.chat.id
        status = message.text
        user = user_dict[chat_id]
        if status in statusspisok:
            user.status = statusspisok[status]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Среднее', 'Специальное', 'Неоконченное высшее', 'Высшее')
            msg = bot.reply_to(message, 'Образование', reply_markup=markup)
            bot.register_next_step_handler(msg, process_education_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_status_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 41')




def process_education_step(message):
    try:
        chat_id = message.chat.id
        education = message.text
        user = user_dict[chat_id]
        if education in educationspisok:
            user.education = educationspisok[education]
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Да, на короткий срок','Да, на длительный срок', 'Нет')
            msg = bot.reply_to(message, 'Готовность к командировкам', reply_markup=markup)
            bot.register_next_step_handler(msg, process_trips_step)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_education_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 42')




def process_trips_step(message):
    try:
        chat_id = message.chat.id
        trips = message.text
        user = user_dict[chat_id]
        if trips in tripsspisok:

            user.trips = tripsspisok[trips]
            markup = types.InlineKeyboardMarkup(row_width=2)
            for i in hobbyspisok:
                itemi = types.InlineKeyboardButton(text = i, callback_data= f'h{hobbyspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id,
                             'Сейчас нужно будет выбрать несколько вариантов. Когда захотите продолжить - внизу будет кнопка "Далее"',
                             reply_markup=types.ReplyKeyboardRemove())
            time.sleep(3)
            bot.send_message(chat_id, 'Укажитe ваши хобби', reply_markup=markup)
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_trips_step)
            return
    except Exception as e:
        bot.reply_to(message,
                     'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(message.text, 'Код 43')


@bot.callback_query_handler(func = lambda callback: callback.data.startswith('h'))
def process_hobby_step(callback):
        chat_id = callback.from_user.id
        hobby = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup(row_width=2)
        if hobby == 'hДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in profspisok:
                itemi = types.InlineKeyboardButton(text=i, callback_data=f'p{profspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Кем ты хочешь стать?', reply_markup=markup)
            user.hobby = list(set(user.hobby))
            print(user.hobby)
        else:
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            user.hobby.append(str(hobby[1:]))
            for i in hobbyspisok:
                itemi = types.InlineKeyboardButton(text=f'{i} ✅' if f'{hobbyspisok[i]}' in user.hobby else i, callback_data=f'h{hobbyspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще хобби или Нажмите "Далее"', reply_markup=markup)
            return




@bot.callback_query_handler(func = lambda callback: callback.data.startswith('p'))
def process_prof_step(callback):
    try:
        chat_id = callback.from_user.id
        prof = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup(row_width=3)
        if prof == 'pДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            msg = bot.send_message(chat_id, 'Укажите ваши профессиональные достижения')
            bot.register_next_step_handler(msg, process_achievments_step)
            user.prof = list(set(user.prof))
            print(user.prof)

        else:
            user.prof.append(str(prof[1:]))
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in profspisok:
                itemi = types.InlineKeyboardButton(
                    text=f'{i} ✅' if f'{profspisok[i]}' in user.prof else i,
                    callback_data=f'p{profspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще профессий или Нажмите "Далее"', reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(chat_id,
                         'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(callback.data)



def process_achievments_step(message):
    try:
        chat_id = message.chat.id
        achievments = message.text
        user = user_dict[chat_id]
        user.achievments = achievments
        msg = bot.reply_to(message, 'Дополнительные навыки')
        bot.register_next_step_handler(msg, process_skills_step)
    except Exception as e:
        bot.send_message(chat_id, 'Что-то пошло не так. Напишите /help или /start')
        print(message.text)


def process_skills_step(message):
    try:
        chat_id = message.chat.id
        skills = message.text
        user = user_dict[chat_id]
        user.skills = skills
        markup = types.InlineKeyboardMarkup()
        for i in artspisok:
            itemi = types.InlineKeyboardButton(text=i, callback_data=f'a{artspisok[i]}')
            markup.add(itemi)
        bot.send_message(chat_id, 'Укажите вашу творческую деятельность', reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, 'Что-то пошло не так. Напишите /help или /start')
        print(message.text)


@bot.callback_query_handler(func = lambda callback: callback.data.startswith('a'))
def process_art_step(callback):
    try:
        chat_id = callback.from_user.id
        art = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup()
        if art == 'aДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in qualitiesspisok:
                itemi = types.InlineKeyboardButton(text=i, callback_data=f'q{qualitiesspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Укажите ваши основные качества', reply_markup=markup)
            user.art = list(set(user.art))
            print(user.art)
        else:
            user.art.append(str(art[1:]))
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in artspisok:
                itemi = types.InlineKeyboardButton(
                    text=f'{i} ✅' if f'{artspisok[i]}' in user.art else i,
                    callback_data=f'a{artspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще или Нажмите "Далее"', reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(chat_id,
                         'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(callback.data)



@bot.callback_query_handler(func = lambda callback: callback.data.startswith('q'))
def process_qualities_step(callback):
    try:
        chat_id = callback.from_user.id
        qualities = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup()
        if qualities == 'qДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in characterspisok:
                itemi = types.InlineKeyboardButton(text= i, callback_data=f'c{characterspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Укажите ваш Характер', reply_markup=markup)
            user.qualities = list(set(user.qualities))
            print(user.qualities)
        else:
            user.qualities.append(str(qualities[1:]))
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in qualitiesspisok:
                itemi = types.InlineKeyboardButton(
                    text=f'{i} ✅' if f'{qualitiesspisok[i]}' in user.qualities else i,
                    callback_data=f'q{qualitiesspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще или Нажмите "Далее"', reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(chat_id,
                         'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(callback.data)



@bot.callback_query_handler(func = lambda callback: callback.data.startswith('c'))
def process_character_step(callback):
    try:
        chat_id = callback.from_user.id
        character = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup()
        if character == 'cДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in typespisok:
                itemi = types.InlineKeyboardButton(text=i, callback_data=f't{typespisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Укажите ваш Тип', reply_markup=markup)
            user.character = list(set(user.character))
            print(user.character)
        else:
            user.character.append(str(character[1:]))
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in characterspisok:
                itemi = types.InlineKeyboardButton(
                    text=f'{i} ✅' if f'{characterspisok[i]}' in user.character else i,
                    callback_data=f'c{characterspisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще или Нажмите "Далее"', reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(chat_id,
                         'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(callback.data)



@bot.callback_query_handler(func = lambda callback: callback.data.startswith('t'))
def process_type_step(callback):
    try:
        chat_id = callback.from_user.id
        type = callback.data
        user = user_dict[chat_id]
        markup = types.InlineKeyboardMarkup()
        if type == 'tДАЛЕЕ':
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Гетеросексуальность', 'Гомосексуальность', 'Бисексуальность')
            msg = bot.send_message(chat_id, 'Сексуальная ориентация', reply_markup=markup)
            bot.register_next_step_handler(msg, process_orientation_step)
            user.type = list(set(user.type))
            print(user.type)

        else:
            user.type.append(str(type[1:]))
            bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)
            for i in typespisok:
                itemi = types.InlineKeyboardButton(
                    text=f'{i} ✅' if f'{typespisok[i]}' in user.type else i,
                    callback_data=f't{typespisok[i]}')
                markup.add(itemi)
            bot.send_message(chat_id, 'Добавьте еще или Нажмите "Далее"', reply_markup=markup)
            return
    except Exception as e:
        bot.send_message(chat_id,
                         'Что-то сломалось или на стороне сервера произошла ошибка. Напишите /help или /start что бы начать сначала')
        print(callback.data)



def process_orientation_step(message):
    try:
        chat_id = message.chat.id
        orientation = message.text
        user = user_dict[chat_id]
        if orientation == 'Гетеросексуальность':
            user.orientation = '1472'
        elif orientation == 'Гомосексуальность':
            user.orientation = '1474'
        elif orientation == 'Бисексуальность':
            user.orientation = '1476'
        else:
            msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
            bot.register_next_step_handler(msg, process_orientation_step)
            return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Да', 'Нет')
        msg = bot.reply_to(message, 'Осталось всего пару шагов. Готовы ли вы к рекламе нижнего белья?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_under_step)
    except Exception as e:
        bot.send_message(chat_id, 'Что-то пошло не так. Напишите /help или /start')
        print(message.text)



def process_under_step(message):
    chat_id = message.chat.id
    under = message.text
    user = user_dict[chat_id]
    if under == 'Да' or under == 'Нет':
        if under == 'Да':
            user.under = '702'
        elif under == 'Нет':
            user.under = '704'
        msg = bot.reply_to(message, 'Загрузите ваше фото. !Внимание! Загружайте только одно фото, и не отправляйте его в виде файла', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, handle_docs_photo)
    else:
        msg = bot.reply_to(message, 'Выберите один из предложенных вариантов')
        bot.register_next_step_handler(msg, process_under_step)
        return


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
        chat_id = message.chat.id
        user = user_dict[chat_id]
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        encoded_string = base64.b64encode(downloaded_file)
        msg = bot.reply_to(message, 'Спасибо, ваша анкета на рассмотрении. Предлагаем вам подписаться на группу вк: https://vk.com/mos_dm')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = {'fields': {
                'NAME': user.name,
                'UF_CRM_1628506279': user.city,
                'SOURCE_ID': 'UC_245OH8',
                'PHONE': [{"VALUE": user.phone, "VALUE_TYPE": "WORK"}],
                'EMAIL': [{"VALUE": user.email, "VALUE_TYPE": "WORK"}],
                'UF_CRM_T_SSYLKANASOC': user.social,
                'UF_CRM_1628805417': {"fileData": [f'Дада image_file.jpg', str(encoded_string)[2:-1]]},
                'UF_CRM_1628012402': user.sex,
                'BIRTHDATE': user.birthdate,
                'UF_CRM_1629229853': user.age,
                'UF_CRM_1628804126': user.relationship,
                'UF_CRM_1628804713': user.kids,
                'UF_CRM_1628804986': user.trips,
                'UF_CRM_1627590723': [user.citizenship],
                'UF_CRM_1627589901': user.passport,
                'UF_CRM_1629237872': [user.language],
                'UF_CRM_T_PROFESSIONA': user.language2,
                'UF_CRM_1628801734': user.person,
                'UF_CRM_1629237675': user.race,
                'UF_CRM_1628801990': user.skin,
                'UF_CRM_1629230716': user.face,
                'UF_CRM_1629236858': user.nose,
                'UF_CRM_1629231263': [user.eyes],
                'UF_CRM_1628801902': user.eyecolor,
                'UF_CRM_1630579845': [user.lips],
                'UF_CRM_1628802115': user.hair,
                'UF_CRM_1629230810': user.hairstyle,
                'UF_CRM_1628802217': user.hairlength,
                'UF_CRM_1629230008': user.height,
                'UF_CRM_1628802392': user.height2,
                'UF_CRM_1628802811': user.shoes,
                'UF_CRM_1628802517': user.clothes,
                'UF_CRM_1629230103': user.constitution,
                'UF_CRM_1628802611': user.waist,
                'UF_CRM_1628802735': user.hips,
                'UF_CRM_1628802909': user.bust,
                'UF_CRM_1628803011': user.breast,
                'UF_CRM_1629237578': [user.cosmetic],
                'UF_CRM_1629237486': [user.cosmetology],
                'UF_CRM_1627589850': user.tattoo,
                'UF_CRM_1629237039': user.stomato,
                'UF_CRM_1629237136': [user.speech],
                'UF_CRM_1629237245': [user.facehair],
                'UF_CRM_1629237308': user.bodyhair,
                'UF_CRM_1629239167': [user.status],
                'UF_CRM_1629239095': [user.education],
                'UF_CRM_1629238198': user.hobby,
                'UF_CRM_1627586659': user.prof,
                'UF_CRM_1628803639': user.achievments,
                'UF_CRM_1628803565': user.skills,
                'UF_CRM_1629238306': user.art,
                'UF_CRM_1629237984': user.qualities,
                'UF_CRM_1629238087': user.character,
                'UF_CRM_1629238156': user.type,
                'UF_CRM_1628804410': user.under,
                'UF_CRM_1629239229': user.orientation
            }}
        b = fast_bitrix24.Bitrix('bitrix_api_link-key')
        with b.slow():
            results = b.call('crm.lead.add', tasks)






bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()
