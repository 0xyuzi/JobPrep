[103 · Linked List Cycle II](https://www.lintcode.com/problem/103/?_from=ladder&fromId=161)

- Use "fast and slow ptrs" method.
- Think about the two distance (one is the distance from the head to the entry of the circle "a", another is the cycle length "b".)
- When two ptrs first met, the relationship between their steps w.r.t the a and b.
- Step back the fast to the head and go over with slow in only one step each time. When They meet again, this node is the entry point.

[Detail solution from leetcode.cn](https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/)

