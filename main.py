from stats import get_word_count, get_char_count, sort_character_count
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        book = f.read()
    return book

def main():

    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_text = get_book_text(book_path)
    char_dict: dict[str, int] = get_char_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words.")
    print("--------- Character Count -------")
    sort_character_count(char_dict)
    print("============= END ===============")
main()