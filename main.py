from stats import count_words, count_letters, sort_letter_counts
import sys

# initialization and check for bookpath, return error message if not found
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# set bookpath
book_location = sys.argv[1]


# Function to take in file path to book outputs text in string format
def get_book_text(path_to_file):  # remember that path_to_file is a string
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


# Main function
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(book_location))} total words.")
    print("----------- Letter Count ----------")
    # print(sort_letter_counts(count_letters(get_book_text(book_location))))
    sorted = sort_letter_counts(count_letters(get_book_text(book_location)))
    for e in sorted:
        if e[0].isalpha():
            print(f"{e[0]}: {e[1]}")
    print("============= END ===============")


main()
