import sys
from stats import (
    get_word_count,
    get_char_count,
    get_sorted_count
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_count = get_sorted_count(char_count)
    print_report(path, word_count, sorted_count)


def get_book_text(file):
    with open(file) as book:
        return book.read()


def print_report(path, word_count, sorted_count):
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for pair in sorted_count:
        if pair["letter"].isalpha():
            print(f"{pair['letter']}: {pair['count']}")
    print("============= END ===============")


main()