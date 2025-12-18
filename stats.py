def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8-sig") as f:
        return f.read()


def get_number_of_words(book: str) -> str:
    text = get_book_text(book)
    num_of_words = text.split()
    return f"Found {len(num_of_words)} total words"


def count_num_characters(book: str) -> dict:
    text = get_book_text(book)
    result = {}
    for letter in text.lower():
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


def sort_dict_of_letters(book: str):
    letters = count_num_characters(book)
    result = []
    for key, value in letters.items():
        if key.isalpha():
            result.append({"name": key, "num": value})
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(items):
    return items["num"]
