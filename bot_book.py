import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.config import BotConfig
from config.menu import set_main_menu
from handlers import main_handlers, other_handlers


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную bot_config
    bot_config = BotConfig()

    # Инициализируем бот и диспетчер
    bot: Bot = bot_config.bot
    dp: Dispatcher = bot_config.ds

    # Настраиваем главное меню бота
    await set_main_menu(bot_config.bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(main_handlers.router_main)
    dp.include_router(other_handlers.router_other)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
