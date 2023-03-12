from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_admins = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Все заявки'),
            KeyboardButton(text='Кто прошел тест'),
            KeyboardButton(text='Скачать отчет.'),
        ],
        [
            KeyboardButton(text='Создать новый пост'),
            KeyboardButton(text='📞 Отправить сообщение всем админам'),
            KeyboardButton(text='✉ Отправить сообщение всем пользователям'),
        ],
        [
            KeyboardButton(text='Вернуться в главное меню.'),
        ],
    ],
    resize_keyboard=True
)
