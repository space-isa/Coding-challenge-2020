#-------------------------------------------------------------------------------
#    Intersecting line segments
#-------------------------------------------------------------------------------
# By Isabel J. Rodriguez
# Daily coding problem
# Completed 04.14.2021
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------
"""
We know that given 4 points: p1, q1, p2, q2 an intersection exists 
if:
 
     (1) p_n < p_n+i AND (2) q_n > q_n+i
     --------------OR-----------------
     (1) p_n > p_n+i AND (2) q_n < q_n+i        for i = 1, 2, 3, ..., N-1

Conversely, if both nodes of a line segment are larger or smaller 
than that of another pair of nodes,

     (1) p_n < p_n+i AND (2) q_n < q_n+i
     --------------OR-----------------
     (1) p_n > p_n+i AND (2) q_n > q_n+i        for i = 1, 2, 3, ..., N-1

then those line segments do not intersect.

This means we are going to have to check combinations of elements  in each list to see 
if this condition for intersecting is satisfied. Something we can leverage in this 
problem is the fact the condition relies on a  binary comparision of two elements 
from the same list. In this way, we can precompute (1) and (2) before checking whether 
the condition for intersecting is met.

Once we have precomputed the different elements in each list, we can then compare our
results from p and q, counting only instances where an element p[i] == q[i] as intersections.

ALGORITHM
---------
1) Ensure both input lists are of the same length.
2) Create an empty binary check list. 
3) Take each list and compare the size of each element against its neighbors:
    - If an element is larger, add a 1 to the binary check array. 
    - Else, add a 0.
4) Initialize a counter.
5) Compare elements pairwise for both binary lists:  
    - If the pairs are not equal, increment the counter by 1.
6) Return the final value of the counter.
"""

import sys

def check_elements(my_list, N):
    """
    Compare size of each element against every other element. 
    Return a list of binary numbers, with 1 signifing an element 
    is larger than its subsequent neighbor, and 0 if it is smaller 
    than its subsequent neighbor.
    """

    binary_check = []
    j = 0
    while j < N-1:
        for i in range(j, N-1):
            if my_list[j] < my_list[i+1]:
                binary_check.append(0)
            else: 
                binary_check.append(1)
        j += 1
    return binary_check

def find_intersection(binary_p, binary_q, len_binary):
    """
    Compare the binary results of both arrays to determine if 
    there are two lines that intersect.
    """
    num_intersections = 0
    for i in range(len_binary-1):
        if binary_p[i] == binary_q[i]:
            num_intersections += 0
        else: 
            num_intersections += 1
    return num_intersections


def main(p, q):
    N = len(p)
    if len(q) != N:
        return ("Your array lengths do not match.")
    binary_p = check_elements(p, N)
    binary_q = check_elements(q, N)
    len_binary = len(binary_p)
    num_intersections = find_intersection(binary_p, binary_q, len_binary)
    print(num_intersections)

if __name__ =="__main__":
    try:
        p = sys.argv[1]
        q = sys.argv[2]
    except Exception as error: 
        print(error)
    main(p, q)
