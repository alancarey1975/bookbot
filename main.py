import sys

from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_dicts

def get_book_text(path_to_file):
    # Open and read the file at the specified path
    with open(path_to_file) as f:
        file_contents = f.read()
    # Return the contents of the file as a string
    return file_contents

def main():
    # Check if exactly one command-line argument (file path) is provided
    if len(sys.argv) != 2:
        # Print usage instructions if argument count is incorrect
        print("Usage: python3 main.py <path_to_book>")
        # Exit the program with an error status
        sys.exit(1)
    
    # Get the file path from the command-line argument
    book_link = sys.argv[1]
    # Read the book text from the file
    book_text = get_book_text(book_link)
    # Calculate the total number of words in the book
    book_nums = get_num_words(book_text)
    # Get the dictionary of character counts
    char_dict = get_num_chars(book_text)
    # Get the sorted list of dictionaries with character counts
    sorted_dicts = get_sorted_dicts(char_dict)
    
    # Print the header for the BookBot report. Display path to book and word count.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_link}...")
    print("----------- Word Count ----------")
    print(f"Found {book_nums} total words")
    print("--------- Character Count -------")
    # Iterate through sorted dictionaries and print counts for alphabetic characters
    for entry in sorted_dicts:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    # Print the footer for the report
    print("============= END ===============")

main()