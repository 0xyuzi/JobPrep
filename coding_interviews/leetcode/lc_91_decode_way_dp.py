class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0
        
        dp = [0]*(len(s)+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s)+1):
            sum_ways = 0
            if self.is_valid_two_digits(s,i):
                sum_ways += dp[i-2]
            if self.is_valid_one_digit(s,i):
                sum_ways += dp[i-1]
            
            dp[i] = sum_ways
        
        return dp[len(s)]
        
    # check if two digits are valid
    def is_valid_two_digits(self, s,i):
        if 1 <= int(s[i-2:i]) <= 26 and int(s[i-2]) !=0:
            return True
        
        return False 
    
    def is_valid_one_digit(self, s,i):
        if int(s[i-1]) !=0:
            return True
        return False