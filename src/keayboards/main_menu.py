from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛂 Получить информацию'),
            KeyboardButton(text='❕ Пройду ли я к вам?'),
        ],
        [
            KeyboardButton(text='📞 Связаться с нами'),
            KeyboardButton(text='✉ Оставить сообщение'),
        ],
        [
            KeyboardButton(text='❓Узнать статус трудоустройства'),
        ],
    ],
    resize_keyboard=True
)

info_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Про Шереметьево'),
            KeyboardButton(text='Чем предстоит заниматься?'),
        ],
        [
            KeyboardButton(text='Льготы и зарплата'),
            KeyboardButton(text='Наши контакты'),
        ],
        [
            KeyboardButton(text='Вернуться в главное меню.'),
        ],
    ],
    resize_keyboard=True
)


async def contact_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    first_button = KeyboardButton(text="📱 Отправить", request_contact=True)
    markup.add(first_button)
    return markup
