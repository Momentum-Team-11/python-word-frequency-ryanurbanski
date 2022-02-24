import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """This function takes in a file and will print the frequency that
    the non-stop words occur."""
    with open(file) as file:
        lines = file.read()
        print(type(lines))
        print(lines)
    remove_punctuation(lines)


def remove_punctuation(stringWithPunctuation):
    """Removes all punctuation from a string"""
    punctuation_list = string.punctuation
    print(punctuation_list)
    for char in stringWithPunctuation:


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
