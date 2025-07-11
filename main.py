from stats import get_num_words
from stats import get_num_characters

def main():
    num_words = get_num_words("books/frankenstein.txt")
    num_characters = get_num_characters("books/frankenstein.txt")
    print(f"{num_words} words found in the document", num_characters)

main()