from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_link = 'books/frankenstein.txt'
    book_text = get_book_text(book_link)
    book_nums = get_num_words(book_text)
    char_dict = get_num_chars(book_text)
    sorted_dict = get_sorted_dict(char_dict)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {book_nums} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        if char.isalpha():
            amount = sorted_dict[char]
            print(f"{char}: {amount}")
    print("============= END ===============")

main()
