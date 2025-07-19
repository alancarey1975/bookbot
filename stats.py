def get_num_words(book_text):
    # Split the input string into a list of words using whitespace as delimiter
    word_list = book_text.split()
    
    # Calculate the number of words by finding the length of the word list
    num_words = len(word_list)
    
    # Return the total number of words
    return num_words

def get_num_chars(book_text):
    # Initialise an empty dictionary to store character counts
    char_count = {}

    # Convert input string to lowercase to avoid case-sensitive duplicates
    lower_string = book_text.lower()

    # Iterate through each character in the lowercase string
    for char in lower_string:
        # If character exists in dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If character not in dictionary, add it with count of 1
        else:
            char_count[char] = 1

    # Return the dictionary with character counts
    return char_count

def get_sorted_dicts(char_dict):
    # Define a helper function to extract the 'num' value for sorting
    def sort_on(item):
        return item["num"]

    # Initialise an empty list to store dictionaries of character counts
    sorted_dicts = []

    # Convert character count dictionary to a list of dictionaries with 'char' and 'num' keys
    for key, value in char_dict.items():
        sorted_dicts.append({"char": key, "num": value})

    # Sort the list by count in descending order using the sort_on function
    sorted_dicts.sort(reverse=True, key=sort_on)

    # Return the sorted list of dictionaries
    return sorted_dicts