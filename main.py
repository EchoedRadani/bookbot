from stats import get_number_of_words, sort_dict_of_letters
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


book = sys.argv[1]


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(get_number_of_words(book))
    print("--------- Character Count -------")
    for result in sort_dict_of_letters(book):
        print(f"{result["name"]}: {result["num"]}")
    print("============= END ===============")


main()