from typing import TypedDict

def get_word_count(string: str):
    split_str = string.split()
    return len(split_str)

def get_char_count(string: str):
    symbols: dict[str, int] = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in symbols:
            symbols[char] += 1
        else:
            symbols[char] = 1
    return symbols

class CharInfo(TypedDict):
    character: str
    count: int

def sort_character_count(chars: dict[str, int]):
    char_list: list[CharInfo] = []

    for char in chars:
        char_list.append({"character": char, "count": chars[char]})

    char_list.sort(reverse=True, key=sort_func)

    for dictionary in char_list:
        if dictionary["character"].isalpha():
            print(f"{dictionary["character"]}: {dictionary["count"]}")

def sort_func(chars: CharInfo):
    return chars["count"]