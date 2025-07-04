def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_text):
    word_list = book_text.split()
    num_words = len(word_list)
    return num_words

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    print(f"{get_num_words(book_text)} words found in the document")


main()
