# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # rightmost search
        result = []
        self.dfs(root, result, 0, 0, True)
        
        return result 
        
        
    def dfs(self, node, right_views, level, max_right_level, is_right):
        # in-order trasverse mid->right->left
        
        print(level)
        
        if not node and is_right:
            print(f"none node: max_right_level: {max_right_level}")
            return max_right_level
        
        print(level, node.val, level)
        
        if is_right:
            right_views.append(node.val)
            if level > max_right_level:
                max_right_level = level 
                
        else:
            if level > max_right_level:
                right_views.append(node.val)
        
        
        right_max_level = self.dfs(node.right, right_views, level+1, max_right_level, True)
        print(right_max_level)
        # if have node.left 
        if node.left:
            self.dfs(node.left, right_views, level+1, max_right_level, False)
        