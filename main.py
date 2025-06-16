import sys
from stats import count_words
from stats import count_chars
from stats import sort_dict


def get_book_text(filepath):
        with open(filepath) as f:
              content = f.read()
        return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        text = get_book_text(sys.argv[1])
    count = count_words(text)
    number_of_characters = count_chars(text)
    sorted = sort_dict(number_of_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", count, "total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():      
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    return


main()