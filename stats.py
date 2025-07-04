def get_num_words(book_text):
    word_list = book_text.split()
    num_words = len(word_list)
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
