# coding: utf-8
#! /usr/bin/env python3.8
#-------------------------------------------------------------------------------
#    Add up to k
#-------------------------------------------------------------------------------
#    Author: Isabel J. Rodriguez
#-------------------------------------------------------------------------------
"""
PROBLEM
-------
Given a list of numbers and a number k, return whether any two numbers from the 
list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true 
since 10 + 7 is 17.

[Source: Daily Coding Challenge]

SOLUTION APPROACH
----------------- 
1. Validate input (assume positive int and float). 
2. If the list is not empty, create an empty storage set. 
3. For each element in the list, take the difference of k and the element and 
   check if that difference exists in the storage set. 
   - If the value exists, return true and stop traversing the list.
   - Else, add that value to the set, and continue with the next element. 

Notes:
Other solutions would include: 
   - Traversing only a subset of the list containing values less than k (assuming positive). 
     This would involve sorting [O(n log n)], creating a new list [O(len(l1) - len(l2))], 
     and traversing that list O(len(l2)).  
   - Checking each element against every other element. 
 
This approach has a time complexity of O(n), as the worst case the list only 
has to be traversed once. 
"""
import time
from functools import wraps
import random
import numpy as np


def timeit(function):
    """A timing decorator."""
    @wraps(function)
    def timing_wrapper(*args):
        print(function.__name__)
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        runtime = end_time - start_time

        print("A list with {} elements took {} {:.2e} sec to process.".format(len(args[0]), 
                                                                function.__name__, runtime))
        return result
    return timing_wrapper

def draw_random_inputs():
    """Return a list of unique random integers and an integer target."""
    size = np.random.randint(30)
    high = size + np.random.randint(10)
    my_list = np.random.choice(np.arange(0, high), replace=False, size=size)
    print("my_list =", my_list)
    k = np.random.randint(100)
    print("k =",k)
    return my_list, k

@timeit
def find_sums(my_list, k):
    # Validate input
    try:
        if len(my_list) == 0: 
            return ("This list is empty.")
        else:
            elements_checked = 0
            length = len(my_list) 
            stored_values = set()
            for element in my_list:
                elements_checked += 1
                difference = k - element
                # Check for a match 
                if difference in stored_values:
                    print("Target found in {}/{} elements".format(elements_checked, length))
                    return True
                # If no match, add value to set and continue
                else: 
                    stored_values.add(element)
            # Target was not found.
            return ("No match found. Checked {}/{} elements.".format(elements_checked, length))  
    except TypeError:
        raise TypeError("Please use integers or floats.")
    except Exception as error: 
        print(error)
    
def main():
    my_list, k = draw_random_inputs()
    result = find_sums(my_list, k)
    print(result)


if __name__ == "__main__":
    main()
    
