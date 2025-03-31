import sys

from stats import get_num_words
from stats import get_num_letters
from stats import get_sorted_letters

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def print_sorted_letters(sorted_letters):
    for dict in sorted_letters:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["num"]}")        

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    data_to_parse = get_book_text(book_path)
    num_words = get_num_words(data_to_parse)
 
    num_letters = get_num_letters(data_to_parse)
    sorted_letters = get_sorted_letters(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_letters(sorted_letters)
    print("============= END ===============")


main()