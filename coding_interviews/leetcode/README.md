# Coding Problems in Leetcode

## Depth-First-Search
- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
    - DFS framework
    - string concat/join methods
    - Single linked-list node creation 

- [394. Decode String](https://leetcode.com/problems/decode-string/)
    - codding assisted by this [answer](https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/) in leetcode cn
    - recursive dfs
    - the key part is to deal with the conditions when positive int, "[" ,"]" and "string"
    - and deal with when at end of the string
    - need to discuss

- [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
    - solved (need to discuss)
    - [code](./199_binary_tree_right_side_view.py)

- [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
    - solved (need to discuss)
    - [code](./863_all_nodes_distance_k_binary_tree.py)

- [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
    - [dfs solution](./695_max_area_island_dfs.py)
    - need to discuss the dfs solution
    - BFS solvable in [here](./695_Max_Area_of_Island_bfs.py) 
    
## Prepare Interview
- [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
    - [My code practice](./91_decode_ways.py)
    - Recursion + memo 
    - Check the leading 0 case, and the valid of double digits between 10 and 26
    - [Huahua solution much helpful!](https://www.youtube.com/watch?v=OjEHST4SXfE)
    - Could use dynamic programming but could be start with [climb stair problem](https://leetcode.com/problems/climbing-stairs/) to familiar with DP.
    - The climb star problem solved by using DP method. [code](./70_Climbing_Stairs.py)
    - [My code](./lc_91_decode_way_dp.py) Using dp method to solve.
        - the dp[0] and dp[1] initialization 
        - check the valid one digits and valid two digits

- [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
    - Bfs works but if constant extra space, should consider other ways
    - Pre-order method works in this case
    - Be careful about the edge cases(leaf node, None node)
    - [My code practice](./116_populate_next_right_pointer_each_node.py)
    - [Huahua's solution ](https://www.youtube.com/watch?v=YNu143ZN4qU)
    - This problem's variance is [117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

- [117.117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
    - Level-order BFS works but needs to use queue that not in constant O(N)
    - Use linked-list
        - Head node to stay at the first node in each level
        - Tail to go over nodes in the same level
        - Cur to create links from left to right in next level
    - [My code](./117_pop_next_right_point_tree2.py)
    - Nice solution by [Orust](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/117-tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-11/) in Chinese edition

### Recursion
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
    - DFS, adding "(" and ")" into the path,
    - Exit condition: 
        - no more available parenthese for both left and right -> adding path into the result
        - the  available right parenthese less than left parenthese 

-[139. Word Break](https://leetcode.com/problems/word-break/)
    - dfs + memo
    - prefix + dfs(suffix, word_dict, memo)
    - memo[suffix], check if prefix and suffiix in word_dict or not

-[140. Word Break II](https://leetcode.com/problems/word-break-ii/)
    - similar to word break above, but need to output all possible solutions and can use the words in word dict repeatedly
    - need to loop all possible combination  