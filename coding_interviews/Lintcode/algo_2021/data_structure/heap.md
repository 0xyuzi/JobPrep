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

[606 Kth Largest Element II](https://www.lintcode.com/problem/606/?_from=ladder&fromId=161)

- Could use partition method, O(n) in average, but worst case is O(n^2).
- Priority q: two methods
    1. heapify the first k in the array, then use `heappushpop` for the left n-k elements in the array. The time complex is k+(n-k)*log(k)
    2. heapify all the element in the array by multiplying the "-" sign, then `heappop` operation in k times and choose the last popped element and multiply back the "-1".

for partition, the code below:
- use index to point the location of the current two sides instead of copy whole array
- keep in mind the "left" and "right" exceed each other so "left" > "right" after partition. 
- think about the exit conditions

```python
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        # edge cases 
        if not nums or k < 1 or k>len(nums):
            return None 
        
        size = len(nums)
        # partition algo 
        return self.partition(nums, 0,size-1, size-k)
    
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        
        pivot = nums[(end-start)//2+start]
        left, right = start, end 

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 

        if k <= right:
            return self.partition(nums, start, right, k)
        if k>= left:
            return self.partition(nums, left, end, k)

        return nums[k]

```


 two methods of heapq

 ```python
from heapq import heapify, heappushpop
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        min_heap = nums[:k]
        heapify(min_heap)

        # heappushpop
        for num in nums[k:]:
            heappushpop(min_heap, num)

        return min_heap[0]

 ```

 ```python
import heapq


# Heapify
# Time Complexity: O(n + klogn)
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        if not nums or k < 1:
            return None
        
        # O(n)
        nums = [-num for num in nums]    
        # O(n)
        heapq.heapify(nums)
        ans = None
        # O(klogn)
        for _ in range(k):  # O(k)
            ans = -heapq.heappop(nums)  # O(logn)
        return ans

 ```