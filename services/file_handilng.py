BOOK_PATH = 'C:/Users/chaps/Desktop/important/stepik/tg_bot_py/bot_book/book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    if start + page_size <= len(text) - 1:
        part = text[start:page_size + start]
        if part[-1] not in ',.!:;?' or part[-2] in ',.!:;?':
            for i in range(len(part) - 3, -1, -1):
                if part[i] in ',.!:;?' and part[i-1] not in ',.!:;?' and part[i+1] not in ',.!:;?':
                    part = part[:i+1]
                    break
    else:
        part = text[start:]

    return part, len(part)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as book_file:
        book_string = book_file.read()
        gotten_parts_sum = 0
        for page in range((len(book_string) // PAGE_SIZE) + 1):
            temp_page, gotten_part = _get_part_text(book_string, gotten_parts_sum, PAGE_SIZE)
            gotten_parts_sum += gotten_part
            book[page + 1] = temp_page.lstrip()


# Вызов функции prepare_book для подготовки книги из
prepare_book(BOOK_PATH)

print(book)
