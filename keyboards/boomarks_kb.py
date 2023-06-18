from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON
from services.file_handilng import book_prepared


def create_bookmarks_keyboard(bookmarks: set[int]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for bookmark_page in sorted(bookmarks):
        bookmark_button = InlineKeyboardButton(
            text=f'{bookmark_page} - {book_prepared[bookmark_page][:100]}',
            callback_data=str(bookmark_page))
        kb_builder.row(bookmark_button)

    bookmarks_edit_cancel_buttons = [
        InlineKeyboardButton(text=LEXICON['edit_bookmarks_button'], callback_data='edit_bookmarks'),
        InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')
    ]

    kb_builder.row(*bookmarks_edit_cancel_buttons)
    return kb_builder.as_markup()


def create_edit_keyboard(bookmarks: set[int]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    for bookmark_page in sorted(bookmarks):
        cancel_bookmark_button = InlineKeyboardButton(
            text=f'{LEXICON["del"]} {bookmark_page} - {book_prepared[bookmark_page][:100]}',
            callback_data=f'{bookmark_page}del')

        kb_builder.row(cancel_bookmark_button)

    bookmarks_edit_cancel_buttons = InlineKeyboardButton(text=LEXICON['cancel'], callback_data='cancel')
    kb_builder.row(bookmarks_edit_cancel_buttons)

    return kb_builder.as_markup()
