from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # first transverse all nodes to build the dict that {node.val: uppernode} since the target node may not be the root node
        # so need to climb to the upper level 
        # then use bfs to scan the level start from the target
        
        upper_node_dict = {}
        
        self.dfs(root, root, upper_node_dict)
        # print(max_level)
        
        # if K > max_level:
        #     return []
        # for node in upper_node_dict:
        #     print(f"node.val: {node.val} upper_node: {upper_node_dict[node].val}")
        
        target_node = None
        
        for node in upper_node_dict:
            # print(node.val, target.val)
            if node.val == target.val:
                # print("find targget")
                target_node = node
        
#         print(f"targer val: {target_node.val}")
#         print(f"distance: {K}")
      
        # start from target level using bfs level by level to get results
        if K ==0:
            return [target_node.val]
        else:
            return self.bfs(target_node, upper_node_dict, K)
        
        
    
    def dfs(self, node, upper_node, upper_node_dict):
        
        if not node:
            return 
        
        # if max_level < level:
        #     max_level = level
            
        upper_node_dict[node] = upper_node
        
        self.dfs(node.right, node, upper_node_dict)
        self.dfs(node.left, node, upper_node_dict)
        
        
    
    def bfs(self, target_node, upper_node_dict, distance):
        
        level = 0
        visited = set()
        visited.add(target_node.val)
        queue = deque([])
        queue.append(target_node)
        result = []
        
        while(queue):
            if level == distance:
                return result
             
            
            for i in range(len(queue)):
                # print(len(queue))
                node = queue.popleft()
                
                # upper, left, right
                for neighbour_node in [upper_node_dict[node], node.right, node.left]:
                    if neighbour_node != None and neighbour_node.val not in visited:
                        queue.append(neighbour_node)
                        visited.add(neighbour_node.val)
                        result.append(neighbour_node.val)
                        print(neighbour_node.val)
            
            
            level += 1
        
        return []
                    