from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_us_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Служба', callback_data='Сообщение'
            ),
            InlineKeyboardButton(
                text='Видео', callback_data='Трудоустройство'
            ),
        ],
    ],
    row_width=2
)

duty = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Обязанности', callback_data='Обязанности'
            ),
            InlineKeyboardButton(
                text='Ограничения', callback_data='Ограничения'
            ),
        ],
    ],
    row_width=2
)

benefits = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Зарплата', callback_data='Зарплата'
            ),
            InlineKeyboardButton(
                text='Жилищное обеспечение', callback_data='Обязанности'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Порядок начисления пенсии', callback_data='пенсия'
            ),
            InlineKeyboardButton(
                text='Отпуск', callback_data='отпуск'
            ),
        ],
    ],
    row_width=2
)

TEST_USER_CHOICES = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Да', callback_data='1'
            ),
            InlineKeyboardButton(
                text='Нет', callback_data='0'
            ),
        ],
    ],
    row_width=2,
)
