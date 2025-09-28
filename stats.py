# function to take in text string and count number of words
def count_words(text):
    words = text.split()
    return len(words)


# Function to take in text and count number of each letter
def count_letters(text):
    letters = text.lower()
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


# Function that take dictionary of character and counts and returns a sorted list of only letters
def sort_letter_counts(letter_counts):
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts
