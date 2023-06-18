from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON
from services.file_handilng import book_prepared


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for button in sorted(args):
        bookmark_button = InlineKeyboardButton(
            text=f'{button} - {book_prepared[button][:100]}',
            callback_data=str(button))
        kb_builder.row(bookmark_button)

    bookmarks_edit_cancel_buttons = [
        InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks'),
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')
    ]

    kb_builder.row(*bookmarks_edit_cancel_buttons)
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for button in sorted(args):
        cancel_bookmark_button = InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book_prepared[button][:100]}',
            callback_data=f'{button}del')

        kb_builder.row(cancel_bookmark_button)

    bookmarks_edit_cancel_buttons = InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')
    kb_builder.row(bookmarks_edit_cancel_buttons)

    return kb_builder.as_markup()
