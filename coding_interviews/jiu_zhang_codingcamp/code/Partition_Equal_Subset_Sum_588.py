class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        
        if not nums or len(nums)<=1:
            return False 
        
        # print(sum(nums) % 2)
        # check if sum(nums)%2 == 0
        if sum(nums) % 2 !=0:
            return False 
        
        half_sum = sum(nums) // 2
        # initialization dp 
        
        dp = [False] * (half_sum+1)
        
        dp[0] = True 
        
        for num in nums:
            for i in range(half_sum, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
                
                
        return dp[half_sum]