from dataclasses import dataclass


@dataclass
class User:
    current_page: int
    bookmarks: set[int]


class Database:

    def __init__(self):
        self.users: dict[int, User] = dict()

    def add_user(self, user_id):
        self.users[user_id] = User(1, set())

    def get_current_user_page(self, user_id: int) -> int:
        return self.users[user_id].current_page

    def get_user_bookmarks(self, user_id: int) -> set[int]:
        return self.users[user_id].bookmarks

    def add_page_to_user_bookmarks(self, user_id: int, page: int) -> None:
        self.users[user_id].bookmarks.add(page)

    def update_user_current_page(self, user_id: int, page: int) -> None:
        self.users[user_id].current_page = page

    def remove_user_bookmark(self, user_id: int, bookmark_page: int) -> None:
        self.users[user_id].bookmarks.remove(bookmark_page)
