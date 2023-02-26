from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_us_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Презентация аэропорта', callback_data='презентация'
            ),
        ],
    ],
    row_width=2
)

duty = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Обязанности', callback_data='duty_обязанности'
            ),
            InlineKeyboardButton(
                text='Запреты и ограничения', callback_data='duty_запреты'
            ),
        ],
    ],
    row_width=2
)

benefits = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Зарплата', callback_data='benefits_зарплата'
            ),
            InlineKeyboardButton(
                text='Жилищное обеспечение', callback_data='benefits_жилье'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Порядок начисления пенсии', callback_data='benefits_пенсия'
            ),
            InlineKeyboardButton(
                text='Отпуск', callback_data='benefits_отпуск'
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
