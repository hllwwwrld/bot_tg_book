from aiogram.types import BotCommand
from aiogram import Bot

from lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command=command, description=description) for command, description in LEXICON_COMMANDS.items()]

    await bot.set_my_commands(main_menu_commands)
