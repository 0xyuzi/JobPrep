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
    - The climb stair problem solved by using DP method. [code](./70_Climbing_Stairs.py)
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

- [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
    - Use BFS
    - From end to start
    - Convert deadends to hashset 
    - Consider the edge case the target could in deadends

-[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
    - scan lines, create the tuples (start, 1), (end, -1)
    - so, sorted would if have the same time in start and end, end would ahead of the start 
    - accumulate the second element (1 or -1), which indicates number of conferences simultanesouly, 
    - the max of accumulate would the min of number conference room needed.

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


### Grid type problem
- [934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)
    - Must have two islands (all 1's) that separated by zeros
    - First step is use dfs to find one island the mark their lands with all 2's, and push all island points into the queue
    - Last, bfs the queue to expand level by level, if meet 0, change to 2, if meet 1 return the steps    


### Calculator series problems
- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
    - Stack to store the original or processed numbers
    - Deal with different operators (+,-,*,/)
    - Caution when meet minus sign and divide sign 

- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
    - More complex than lc227 by adding the "(" and ")".
    - Using recursion to deal with "(" 
    - Exit condition on ")" and return parameters of sum of number and next index 
    - [Labuladong's calculator method](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484903&idx=1&sn=184beaad36a71c9a8dd93c41a8ba74ac&chksm=9bd7fbefaca072f9beccff92a715d92ee90f46c297277eec10c322bc5ccd053460da6afb76c2&scene=21#wechat_redirect)


### Power of n
- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
    - Trick to x iteratively multiply it self 
    - n iteratively updated by int divided by 2 (//2)
    - when n is an odd number , res updated by multiply with x
    - check the sign of n 

### Heap
- [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
    - heapq structure
    - the heap will always pop the mininum val inside the heap, so if want maximum, use "-" maximum
    - operations:(h=[])
        - heappush(h,num)
        - heappop(h,num)
        - or heapify(list)

### Trie
- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
    - [code](./208_implement_trie_node.py)
    - create a TrieNode class with children dict and is_children bool type 
    - create a find function in Trie class to search the node of prefix by go over from the first character to the last char if exist.


## FB
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
    - First sort the list
    - chert if the last'element in the result list's end >= cur interval's end
        - if yes, update result list last'element end with max(res[-1].end, cur_interval.end)
        - if no, append the cur interval into the result list
        - [huahua](https://www.youtube.com/watch?v=6tLHjei-f0I)

- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
    - Solution in [Leetcode CN](https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcode/)
    - Time O(1), space O(h), h is the height of the tree
    - Since its BST, naturally would use in-order (left-mid-right)
    - Step 1, in initialization, transverse in left-most fashion and use stack to store the transverse points. Better to create the helper function for leftmost transverse 
    - Stpe 2, in next(), pop out the node as, then check if this node has right child (don't care the left child since have been transversed and in the stack already), if has right child, call the helper function to transverse the this right child leftmost.
    - Step3. hasNext(), check if the stack is empty or not.

-[51. N-Queens](https://leetcode.com/problems/n-queens/)
    - dfs with backtracting (append -> dfs -> pop)
    - mistakes on backtracting when in first row
    - rules is on the queue in the next row could not on the same col, or row + col = anyqueue(row + col), or col - row = any_queue(col - row)


