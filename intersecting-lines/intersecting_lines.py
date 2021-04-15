"""
PROBLEM STATEMENT
-----------------

Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 
and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting 
each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

SOLUTION APPROACH
-----------------
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
2) Create a "binary check" list. 
3) Take each list and compare the size of each element against its neighbors:
    - If an element is larger, add a 1 to the binary check array. 
    - Else, add a 0.
4) Initialize a counter.
5) Compare elements pairwise for both binary lists:  
    - If the pairs are not equal, increment the counter by 1.
6) Return the final value of the counter.
"""
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

def find_intersection(p, q, len_binary_check):
    """
    Compare the binary results of both arrays to determine if 
    there are two lines that intersect.
    """
    num_intersections = 0
    for i in range(len_binary_check-1):
        if p[i] == q[i]:
            num_intersections += 0
        else: 
            num_intersections += 1
    return num_intersections


def main(p, q):
    N = len(p)
    if len(p) != N:
        return ("Your array lengths do not match.")
    check_p = check_elements(p, N)
    check_q = check_elements(q, N)
    len_binary_check = len(check_p)
    num_intersections = find_intersection(check_p, check_q, len_binary_check)
    print(num_intersections)

if __name__ =="__main__":
    p = [1,3,2,0]
    q = [4,2,3,1]
    main(p, q)

# NOTE (turn into formal unit tests): 
# We expect an output of: 
# [0, 0, 1, 1, 1, 1] for p = [1, 3, 2, 0] and 
# [1, 1, 1, 0, 1, 1,] for q = [4, 2, 3, 1]

# We expect: 
# len_binary_check = int((N ** 2 - N) / 2) 