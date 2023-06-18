from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsCallbackFromBookmarks(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.isdigit()


class IsCallbackToEditBookmarks(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data == 'edit_bookmarks'


class IsCallbackByDeletingBookmark(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data[-3:] == 'del'\
               and callback.data[:-3].isdigit()


class IsCallbackFromPage(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        return '_to_bookmark' in callback.data
