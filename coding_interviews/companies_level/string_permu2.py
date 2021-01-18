FALSE = 0 
TRUE = 1

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        s = sorted(list(str))
        res = []
        self.backtrack(s, "", res)
        
        return res 
        
    def backtrack(self, s, permu, permus):
        
        print(s, permu, permus)
        
        if not s:
            permus.append(permu)
            return 
        
        for i in range(len(s)):
            
           
            
            if i !=0 and s[i] == s[i-1]:
                continue 
            
            
            self.backtrack(s[:i]+s[i+1:], permu+s[i], permus )
        
            
if __name__ == "__main__":
    sol = Solution()
    s = "abb"
    print(sol.stringPermutation2(s))


