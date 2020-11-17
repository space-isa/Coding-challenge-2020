
# coding: utf-8
#! /usr/bin/env python3.8
#-------------------------------------------------------------------------------
#    Add up to k (Binary Search Tree)
#-------------------------------------------------------------------------------
#    Author: Isabel J. Rodriguez
#-------------------------------------------------------------------------------
"""
PROBLEM
-------
Given the root of a binary search tree, and a target K, return two nodes in the 
tree whose sum equals K. For example, given the following tree and k of 20,

       10
       /   \
    5       15
             /  \
          11    15

return 5 and 15.

[Source: Daily Coding Challenge]

SOLUTION APPROACH
----------------- 
1) From a constructor class, create BST using predetermined input. 

2) Starting from the root, check the children nodes and see if their sum adds up to the target K. 

3) If not, move on to the next node and repeat. 

4) If after reaching the leaf nodes we have not found a pair of nodes that add up to the target, return NULL. 

5) If we find the target, return the values of the two nodes.
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

# ## What we know: 

# - Inputs: a number and a tree
# - Output: two numbers   

# About binary search tree: 
# - binary => at most two connections from each node
# - For a child node: 
#     - L: smaller value than parent
#     - R: larger value than parent

# ### Q&As (questions and assumptions):  

# - A: Using integer values for each node.
# - Q: How to build tree s.t. the nodes can be easily changed with an input array.
 
# ### Cases to consider: 
# 1) No pair exists 

import numpy as np 

class treeNode: 
    def __init__(self, value=None):
        self.value = value
        # Point to left node 
        self.left_child = None
        # Point to right node  
        self.right_child = None

    def __str__(self):
        return('Node {}: left = {}, right = {}'.format(self.value, 
                                                       self.left_child, 
                                                       self.right_child))

class BinarySearchTree: 
    def __init__(self):
        self.root = None

    def __str__(self):
        return('From BST: root= {}'.format(self.root))
    
    def insert(self, value):
        """Create a new root. If a root exist, insert nodes."""

        if self.root == None:
            # Create a new instance of the treeNode class
            self.root = treeNode(value)
        else: 
            self._insert(value, self.root) 

    def _insert(self, value, current_node):
        """Sort and insert children nodes."""

        if value < current_node.value:
            if current_node.left_child == None: 
                current_node.left_child = treeNode(value)
            else: 
                self._insert(value, current_node.left_child)  
        else: 
            if current_node.right_child == None: 
                current_node.right_child = treeNode(value)
            else:
                self._insert(value, current_node.right_child) 

    '''An in-order traversal to check whether the BST has been set up correctly.'''       
    def printBST(self):
        if self.root != None: 
            self._printBST(self.root)
             
    def _printBST(self, current_node):
        if current_node != None:
            self._printBST(current_node.left_child)
            print('In-order traversal: {}'.format(current_node.value))
            self._printBST(current_node.right_child)

    def checkChildren(self):
        if self.root != None: 
            self._checkChildren(self.root)

    def _checkLeft (self,current_node):
        if current_node != None:
            self.root = current_node
            print('Checking left side. Current node {}'.format(current_node))
            print(self.root.left_child)
            if isinstance(self.root.left_child.value, type(None)):
                if isinstance(self.root.right_child.value, type(None)):
                    print ('This is a leaf.')
            elif self.root.left_child or self.root.right_child == None:
                print ('There is no pair.')
            else:
                print('Left of current node: {}'.format(self.root.left_child))
                print('Right of current node: {}'.format(self.root.right_child))
                if self.root.left_child.value + self.root.right_child.value == 20: 
                    print ('Huzzah!')
        else:
            print('Reached the end of the tree.')
    
    def _checkRight(self, current_node):
        if current_node != None:
            self.root = current_node
            print('Checking right side. Current node {}'.format(current_node))
            print(self.root.left_child.value)
            print(self.root.right_child.value)
            if isinstance(self.root.left_child, type(None)):
                if isinstance(self.root.right_child, type(None)):
                    print ('This is a leaf.')

            elif self.root.left_child or self.root.right_child == None:
                print ('There is no pair.')
            else: 
                print('Left of current node: {}'.format(self.root.left_child))
                print('Right of current node: {}'.format(self.root.right_child))
                if self.root.left_child.value + self.root.right_child.value == 20: 
                    print ('Huzzah! The values are {} & {} '.format(self.root.left_child.value,self.root.right_child.value ))
        else: 
            print('Reached the end of the tree.')
    
    def _checkChildren(self, current_node):
        if current_node != None:
            left_child = self._checkLeft(current_node=current_node.left_child)
            right_child =  self._checkRight(current_node=current_node.right_child)
            if current_node.left_child.value and current_node.right_child.value != None:
                print(current_node.left_child.value + current_node.right_child.value)
                if current_node.left_child.value  + current_node.right_child.value  == 20:
                    print('Left of current node: {}'.format(current_node.left_child.value))
                    print('Right of current node: {}'.format(current_node.right_child.value))
                    print ('Huzzah! The values are {} & {} '.format(self.root.left_child.value,self.root.right_child.value ))
                else:


        return left_child, right_child


def buildTree(input_BST):
    tree = BinarySearchTree()
    for i in range(len(input_BST)):
        tree.insert(input_BST[i])
    print(tree.checkChildren())