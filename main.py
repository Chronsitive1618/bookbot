import sys
from stats import (count_words,
                    sort_dict)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path = sys.argv[1]
        line1 = "============ BOOKBOT ============"
        line2 = f"Analyzing book found at {book_path}..."
        line3 = "----------- Word Count -----------"
        line4 = f"Found {count_words(book_path)} total words"
        line5 = "--------- Character Count ---------"
        end_line = "============= END ==============="
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        char_dict = sort_dict(book_path)
        for unique_dict in char_dict:
            if unique_dict["char"].isalpha() == True:
                letter_line = f"{unique_dict["char"]}: {unique_dict["num"]}"
                print(letter_line)
            else:
                pass
        print(end_line)

main()