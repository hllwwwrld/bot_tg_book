from aiogram import Router
from aiogram.types import Message


router_other = Router()


@router_other.message()
async def process_other_messges(message: Message):
    await message.answer('Такой команды пока нет')