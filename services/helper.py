from database.database import users_db


def get_current_user_page(user_id: int) -> int:
    return users_db[user_id]['page']


def get_user_bookmarks(user_id: int) -> set[int]:
    return users_db[user_id]['bookmarks']


def add_page_to_user_bookmarks(user_id: int, page: int) -> None:
    users_db[user_id]['bookmarks'].add(page)
