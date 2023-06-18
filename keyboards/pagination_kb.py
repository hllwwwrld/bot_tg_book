from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON


# def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     buttons_for_kb = [InlineKeyboardButton(text=LEXICON.get(button, button),
#                                            callback_data=button) for button in buttons]
#     kb_builder.row(*buttons_for_kb)
#     return kb_builder.as_markup()


def create_pagination_keyboard(page_num: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.add(InlineKeyboardButton(text=LEXICON['backward'], callback_data='backward'))
    kb_builder.add(InlineKeyboardButton(text=page_num, callback_data=page_num))
    kb_builder.add(InlineKeyboardButton(text=LEXICON['forward'], callback_data='forward'))
    return kb_builder.as_markup()
