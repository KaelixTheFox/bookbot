import sys
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_characters\
   

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_num_words(sys.argv[1])
    num_characters = get_num_characters(sys.argv[1])
    sorted_characters = get_sorted_characters(num_characters)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count -------")
    for i in range(0, len(sorted_characters)):
        print(sorted_characters[i]["char"], sorted_characters[i]["num"], sep= ": ")    
    print("============= END ===============")

main()