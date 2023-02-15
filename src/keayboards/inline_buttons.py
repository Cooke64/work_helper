from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_us_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Служба', callback_data='сообщение'
            ),
            InlineKeyboardButton(
                text='Как стать ильнуром', callback_data='трудоустройство'
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
