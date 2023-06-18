from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery

from copy import deepcopy

from lexicon.lexicon import LEXICON
from database.database import (user_dict_template, users_db,
                               get_user_bookmarks,
                               get_current_user_page,
                               add_page_to_user_bookmarks,
                               update_user_current_page,
                               remove_user_bookmark)
from services.file_handilng import book_prepared
from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.boomarks_kb import create_bookmarks_keyboard, create_edit_keyboard
from filters.filters import (IsCallbackFromPage,
                             IsCallbackFromBookmarks,
                             IsCallbackByDeletingBookmark,
                             IsCallbackToEditBookmarks)

router_main = Router()


@router_main.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON['/start'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


@router_main.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


@router_main.message(Command(commands=['beginning']))
async def process_beginning_command(message: Message):
    update_user_current_page(message.from_user.id, 1)
    text = book_prepared[get_current_user_page(message.from_user.id)]
    await message.answer(text=text,
                         reply_markup=
                         create_pagination_keyboard(1)
                         )


@router_main.message(Command(commands=['continue']))
async def process_continue_command(message: Message):
    user_page = get_current_user_page(message.from_user.id)
    text = book_prepared[user_page]
    await message.answer(text=text,
                         reply_markup=
                         create_pagination_keyboard(user_page)
                         )


@router_main.message(Command(commands=['bookmarks']))
async def process_bookmark_command(message: Message):
    user_bookmarks = get_user_bookmarks(message.from_user.id)
    if user_bookmarks:
        await message.answer(LEXICON['/bookmarks'], reply_markup=create_bookmarks_keyboard(user_bookmarks))
    else:
        await message.answer(LEXICON['no_bookmarks'])


@router_main.callback_query(IsCallbackFromBookmarks())
async def open_bookmark(callback: CallbackQuery):
    text = book_prepared[int(callback.data)]
    await callback.message.answer(text=text,
                                  reply_markup=create_pagination_keyboard(int(callback.data))
                                  )


@router_main.callback_query(IsCallbackToEditBookmarks())
async def edit_bookmarks(callback: CallbackQuery):
    user_bookmarks = get_user_bookmarks(callback.from_user.id)
    await callback.message.edit_text(text=LEXICON['edit_bookmarks'],
                                     reply_markup=create_edit_keyboard(user_bookmarks))
    await callback.answer()


@router_main.callback_query(IsCallbackByDeletingBookmark())
async def delete_user_bookmark(callback: CallbackQuery):
    remove_user_bookmark(int(callback.from_user.id),
                         int(callback.data[:callback.data.index('d')])
                         )
    user_bookmarks = get_user_bookmarks(callback.from_user.id)
    if len(user_bookmarks) > 0:
        await callback.message.edit_text(text=LEXICON['edit_bookmarks'],
                                         reply_markup=create_edit_keyboard(user_bookmarks))
    else:
        await callback.message.edit_text(LEXICON['no_bookmarks'])

    await callback.answer()


@router_main.callback_query(IsCallbackFromPage())
async def add_page_to_bookmark(callback: CallbackQuery):
    add_page_to_user_bookmarks(int(callback.from_user.id),
                               int(callback.data[:callback.data.find('_')])
                               )
    await callback.answer(text='Страница успешно добавлена в закладки')


@router_main.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    user_page = get_current_user_page(callback.from_user.id)
    if user_page < len(book_prepared):
        new_user_page = user_page + 1
        update_user_current_page(callback.from_user.id, new_user_page)
        text = book_prepared[new_user_page]
        await callback.message.edit_text(text=text,
                                         reply_markup=create_pagination_keyboard(new_user_page))
        await callback.answer()
    else:
        await callback.answer(text='Вы на последней странице')


@router_main.callback_query(lambda callback: callback.data == 'backward')
async def process_backward_press(callback: CallbackQuery):
    user_page = get_current_user_page(callback.from_user.id)
    if user_page > 1:
        new_user_page = user_page - 1
        update_user_current_page(callback.from_user.id, new_user_page)
        text = book_prepared[new_user_page]
        await callback.message.edit_text(text=text,
                                         reply_markup=create_pagination_keyboard(new_user_page)
                                         )
        await callback.answer()

    else:
        await callback.answer(text='Вы на начальной странице')


@router_main.callback_query(Text(text='cancel'))
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.answer(text=LEXICON['cancel_text'])
    await callback.answer()
