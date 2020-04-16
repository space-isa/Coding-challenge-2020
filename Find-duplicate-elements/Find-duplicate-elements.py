
# coding: utf-8
#! /usr/bin/env python3

import numpy as np
from collections import Counter
import random


def findDuplicates(my_array):
    '''This function creates a dictionary containing the number of each element
    then returns the elements that occur more than once.'''
    if len(my_array) == 0:
        return ('This array is empty!')
    else:
        duplicates = []
        counter = Counter(my_array)
    for element in counter:
        if counter[element] >= 2:
            duplicates.append(element)
    return duplicates


def createArray(num_elements):
    my_array = np.random.randint(1, 100, num_elements)
    return my_array


def main():
    my_array = createArray(num_elements=np.random.randint(0, 10000))
    duplicates = findDuplicates(my_array)
    print("There are {} duplicate elements.".format(len(duplicates)))


if __name__ == "__main__":
    main()
