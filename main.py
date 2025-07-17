import sys

from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_dicts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_link = sys.argv[1]
    book_text = get_book_text(book_link)
    book_nums = get_num_words(book_text)
    char_dict = get_num_chars(book_text)
    sorted_dicts = get_sorted_dicts(char_dict)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {book_nums} total words")
    print("--------- Character Count -------")
    for entry in sorted_dicts:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
