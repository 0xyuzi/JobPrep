"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# pre-order traverse
# then use binary tree properties to link:  node.left.next = node.right, node.right.next = node.next.left

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root or not root.left:
            return root
        
        print(root.val)
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root
    
    