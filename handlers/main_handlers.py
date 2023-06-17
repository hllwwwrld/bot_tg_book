from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from lexicon.lexicon import LEXICON

router_main = Router()


@router_main.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON['/start'])


@router_main.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])
