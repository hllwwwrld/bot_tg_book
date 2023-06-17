import configparser

from aiogram import Bot, Dispatcher


config = configparser.ConfigParser()
config.read('C:/Users/chaps/Desktop/important/stepik/tg_bot_py/bot_book/config/config_data')


class BotConfig:
    def __init__(self):
        self.token: str = config.get('BotBook', 'token')
        self.admin_ids: list[int] = list(map(int, config.get('BotBook', 'admin_ids').split(',')))
        self.bot: Bot = Bot(token=self.token, parse_mode='HTML')
        self.ds = Dispatcher()


