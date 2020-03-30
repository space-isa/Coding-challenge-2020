import sys


def findOrderedWords(filename):
    '''This function takes a .txt file as an input and prints all the words that are in alphabetical order.'''
    assert filename.split('.')[1] == 'txt', "Please use a .txt file."
    with open(filename) as data_file:
        data = data_file.read()
        assert (len(data) == 0) == False, "There's nothing in this file."
        # If a line remains unchanged after sorting, it can be printed.
        for line in data.splitlines():
            if line == ''.join(sorted(line)):
                print(line)


def main():
    if len(sys.argv) == 2:
        filename = str(sys.argv[1])
    else:
        raise ValueError(
            "This script takes 2 command-line arguments. You have passed {}.".
            format(len(sys.argv)))
    findOrderedWords(filename)


if __name__ == "__main__":
    main()