# Heap

[130 Heapify](https://www.lintcode.com/problem/130/?_from=ladder&fromId=161)

Use sift down method to get O(n) heapify process (better than sift up O(nlogn)). The detail explanation [here](https://blog.csdn.net/lighthear/article/details/79945528) 
The [code example](https://www.lintcode.com/problem/130/solution?_from=ladder&fromId=161) as 


```python
/**
 * This reference program is provided by @jiuzhang.com
 * Copyright is reserved. Please indicate the source for forwarding
 */

class Solution:
    
    def heapify(self, nums):
        
        for i in reversed(range((len(nums))//2)):
            self.sift_down(nums, i)
            
    def sift_down(self, nums, index):
        
        n = len(nums)
        while index * 2 + 1 < n:
            
            son_index = index * 2 + 1 
            if son_index + 1 < n and nums[son_index] > nums[son_index+1]:
                son_index = son_index + 1 
            if nums[son_index] >= nums[index]:
                break
            nums[index], nums[son_index] = nums[son_index], nums[index]
            index = son_index


```