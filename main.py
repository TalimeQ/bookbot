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
    data_to_parse = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(data_to_parse)
 
    num_letters = get_num_letters(data_to_parse)
    sorted_letters = get_sorted_letters(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_letters(sorted_letters)
    print("============= END ===============")


main()