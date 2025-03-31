def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def get_num_words(parsed_string):
    words_array = parsed_string.split()
    return len(words_array)

def main():
    data_to_parse = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(data_to_parse)
    print(f"{num_words} words found in the document")


main()