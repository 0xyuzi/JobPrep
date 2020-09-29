class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # rightmost search
        if not root:
            return []
        result = [root.val]
        self.dfs(root, result, 0, 0, True)
        
        return result 
        
        
    def dfs(self, node, right_views, level, max_right_level, is_right):
        # in-order trasverse mid->right->left
        
        
        
        if not node and is_right:
            # print(f"none node: max_right_level: {max_right_level}")
            return max_right_level
        
        # print(node.val, right_views, level, max_right_level)
        # print(level, node.val, level)
        
        if is_right:
            
            if level > max_right_level:
                print(level, max_right_level)
                right_views.append(node.val)
                max_right_level = level 
                
                
        else:
            if level > max_right_level:
                print(level, max_right_level)
                right_views.append(node.val)
                max_right_level = level 
        
        
        right_max_level = self.dfs(node.right, right_views, level+1, max_right_level, True)
        # if have node.left 
        if node.left:
            
            # print(node.val, right_max_level)
            right_max_level = self.dfs(node.left, right_views, level+1, right_max_level, False)
        
        return right_max_level
        