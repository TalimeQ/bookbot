def get_num_words(parsed_string):
    words_array = parsed_string.split()
    return len(words_array)

def get_num_letters(parsed_string):
    letters_dict = {}
    for letter in parsed_string:
        lowered = letter.lower()
        if lowered in letters_dict:
            letters_dict[lowered] += 1
        else:
            letters_dict[lowered] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_letters(parsed_dict):
    sorted_list = []
    for key in parsed_dict:
        sorted_list.append({"character": key, "num": parsed_dict[key]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list