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
    lines = remove_punctuation(lines)                   # Puncuation removed
    lines = lines.lower()                               # Sting 'lower-cased'
    lines = lines.split()                               # String converted into a List of words
    lines = remove_stop_words(lines, STOP_WORDS)        # Stop words removed 
    lines = list_to_dictionary(lines)                   # List converted to Dictionary with word count
    lines = sort_by_count(lines)                        # Dictionary sorted in decending order
    print_dictionary(lines)


def print_dictionary (dictToPrint):
    for word, count in dictToPrint.items():
        starString = ""
        j = 0
        while j < count:
            starString += "*"
            j += 1
        print("{} | {} {}".format(word.rjust(15," "), str(count).ljust(3, " "), starString))


def sort_by_count(dictToSort):
    """Sorts a dictionary in descending order of the values for each key"""
    sorted_dict = dict(sorted(dictToSort.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def list_to_dictionary(list):
    """Takes a list and converts it to a dictionary with the list 
    items as the key and all the initial values set to 0"""
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


def remove_stop_words(list1, list2):
    """Takes 2 lists as arguments and will return the first list
    without any elements from list2 """
    finalList = []
    for word in list1:
        if word not in list2:
            finalList.append(word)
    return finalList


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
