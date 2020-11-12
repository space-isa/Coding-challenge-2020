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
1. Validate input (assume int and float). 
2. If the list is not empty, create an empty storage set. 
3. For each element in the list, take the difference of k and the element and 
   check if that difference exists in the storage set. 
   - If the value exists, return true and stop traversing the list.
   - Else, add that value to the set, and continue with the next element. 

Notes:
Other solutions would include: 
   - Traversing only a subset of the list containing values less than k. This 
     would involve sorting [O(n log n)], creating a new list [O(len(l1) - len(l2))], 
     and traversing that list O(len(l2)).  
   - Checking each element against every other element. 
 
This approach has a time complexity of O(n), as the worst case the list only 
has to be traversed once. 
"""
    
def find_sums(my_list=None, k=None):
    # Validate input
    try:
        if (my_list or k == None) == True: 
            return("Please provide a list of numbers and a target value.")
        elif len(my_list) == 0: 
            return("This list is empty.")
        else: 
            stored_values = set()
            for i in range(len(my_list)):
                test_value = my_list[i]
                difference = k - test_value
                # Check for a match 
                if difference in stored_values:
                    return True
                    break
                # If no match, add value to set and continue
                stored_values.add(my_list[i])  
    except TypeError:
        raise TypeError("Please use integers or floats.")
    except Exception as error: 
        print(error)


if __name__ == "__main__":
    find_sums(my_list ,k)
