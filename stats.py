def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
    word_string = get_book_text(path)
    return len(word_string.split())
   
def count_char(path):
    word_string = get_book_text(path)
    word_lowered = word_string.lower()
    character_count = {}
    for character in word_lowered:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sort_dict(path):
    char_dict = count_char(path)
    dict_list = []
    for key in char_dict:
        d = {}
        d["char"] = key
        d["num"] = char_dict[key]
        dict_list.append(d)
        dict_list.sort(reverse=True, key=sort_on)
    return dict_list
