def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents


def main():
    data_to_print = get_book_text("books/frankenstein.txt")
    print(data_to_print)


main()