from aiogram.types import BotCommand


async def set_commands(dp):
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помочь"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await dp.bot.set_my_commands(commands)
