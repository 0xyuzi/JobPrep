# Coding Practices from Jiu Zhang Coding Camp
The coding problems are from [Lintcode](https://www.lintcode.com/)
## DFS Problems

[1514. Robot Room Cleaner (hard level)](https://www.lintcode.com/problem/robot-room-cleaner/description?_from=ladder&&fromId=160) 
- [Code](./code/robot_room_cleaner_1514.py)

[815. Course Schedule IV (hard level)](https://www.lintcode.com/problem/course-schedule-iv/description) 
- [code example from solution](./code/course_schedule_IV_815_example_sol.py)
- [backtracking method explanation (in chinese)](https://segmentfault.com/a/1190000006121957) 
- [bitmap explanation (in chinese)](https://www.cnblogs.com/cjsblog/p/11613708.html)



## DP Problem
[92. Backpack](https://www.lintcode.com/problem/backpack/description?_from=ladder&&fromId=160)
- [Code](./code/Backpack_92.py)
- `dp[i][j]`, the max of size when go over to the ith item with backpack at size of j 


[588. Partition Equal Subset Sum](https://www.lintcode.com/problem/partition-equal-subset-sum/description?_from=ladder&&fromId=160)
- [Code](./code/Partition_Equal_Subset_Sum_588.py)
- True/False
- `for i in range(half_sum, num-1, -1)`

[1861. Rat Jump](https://www.lintcode.com/problem/rat-jump/description?_from=ladder&&fromId=160)
- need to code again
- `% MOD_NUM = 10**9 + 7`
- odds, evens
