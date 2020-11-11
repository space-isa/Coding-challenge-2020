
# coding: utf-8
#! /usr/bin/env python3
#-------------------------------------------------------------------------------
#    Find Duplicate Elements
#-------------------------------------------------------------------------------
#    Author: Isabel J. Rodriguez
#-------------------------------------------------------------------------------
"""
Problem: Determine if an input list contains duplicates. 

Solution Approach: 
1. Check if the input list is empty. 
2. If the list is not empty, create a set of unique elements. 
3. Compare the length of the input list against the length of the set. 
   - If the lengths are not equal, the input list contains duplicates.
   - Else, the input list does not contain duplicates.  

Notes: 
The naive solution would be to create a counter variable to count the number 
of times an element was seen in a list. The time complexity of such an approach 
would be O(n) where n is the number of elements in the list. 

On the other hand, the len() function costs O(1) in time complexity. 
"""

import sys 

def findDuplicates(my_list=None):
    """
    Check the length of the input list against the length of the set of unique 
    items in that list. Print whether the list contains duplicates or not. 

    ARGUMENTS
    ---------

       my_list : list 
    
    RETURNS
    -------
        None
    """

    #  Validate input
    if my_list == None:
        print("Please provide an input.")
        sys.exit(1)

    if len(my_list) == 0:
        print('This list is empty.')
    else:
        unique_elements = set(my_list)
        is_equal = len(unique_elements) == len(my_list)

        #  Determine if there are duplicate elements
        if is_equal == True:
            print("There are no duplicate elements in this list.")
        else:
            print("There are duplicate elements in this list.")

        return is_equal

if __name__ == "__main__":
    is_equal = findDuplicates(my_list)
