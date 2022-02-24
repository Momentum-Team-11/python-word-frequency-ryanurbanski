import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """This function takes in a file and will print the frequency that
    the non-'stop words' occur."""
    with open(file) as file:
        lines = file.read()
        print(lines)                            # Starting String
    lines = remove_punctuation(lines)           # Puncuation removed
    lines = lines.lower()                       # Sting 'lower-cased'
    lines = lines.split()                       # String converted into a List of words
    print(lines)


def remove_punctuation(stringWithPunctuation):
    """Removes all punctuation from a string
    and returns another string."""
    punctuation_list = string.punctuation
    for char in stringWithPunctuation:
        if char in punctuation_list:
            stringWithPunctuation = stringWithPunctuation.replace(char, "")
    return stringWithPunctuation


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
