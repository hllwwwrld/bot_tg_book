user_dict_template: dict = {'page': 1,
                            'bookmarks': set()}

users_db: dict = {}


def get_current_user_page(user_id: int) -> int:
    return users_db[user_id]['page']


def get_user_bookmarks(user_id: int) -> set[int]:
    return users_db[user_id]['bookmarks']


def add_page_to_user_bookmarks(user_id: int, page: int) -> None:
    users_db[user_id]['bookmarks'].add(page)


def update_user_current_page(user_id: int, page: int) -> None:
    users_db[user_id]['page'] = page


def remove_user_bookmark(user_id: int, bookmark_page: int) -> None:
    users_db[user_id]['bookmarks'].remove(bookmark_page)
