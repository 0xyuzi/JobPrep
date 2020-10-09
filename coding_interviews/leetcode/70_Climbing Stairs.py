"""
dynamic programming
1. state 
2. transit function: stay, climb1, climb2 

dp[i] the number of distinct ways to climb to the step i 

dp[i-1]

dp[i-2]

dp[i] = dp[i-1] + dp[i-2]

initail condition: dp[0] = 0, dp[1] = 1
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)

        dp[0], dp[1] = 1, 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]