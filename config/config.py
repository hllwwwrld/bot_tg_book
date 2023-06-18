import configparser
import os

from aiogram import Bot, Dispatcher


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_data'))


class BotConfig:
    def __init__(self):
        self.token: str = config.get('BotBook', 'token')
        self.admin_ids: list[int] = list(map(int, config.get('BotBook', 'admin_ids').split(',')))
        self.bot: Bot = Bot(token=self.token, parse_mode='HTML')
        self.ds = Dispatcher()
