from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


def create_pagination_keyboard(*buttons) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_for_kb = [InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button,
                                           callback_data=button) for button in buttons]
    kb_builder.row(*buttons_for_kb)
    return kb_builder.as_markup()
