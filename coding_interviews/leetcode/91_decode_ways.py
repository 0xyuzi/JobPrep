# recursion dfs + memo
class Solution:
    
   
    
    

    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0
        
        self.memo = {}
            
        return self.dfs(0,s)
    
    
    def dfs(self, i, s):
        print(self.memo)
        if i == len(s):
            return 1
        
        if s[i] == '0':
            return 0
        
        if s[i:] in self.memo:
            return self.memo[s[i:]]
        
        if 10<= int(s[i:i+2]) <=26:
            num = self.dfs(i+1,s) + self.dfs(i+2,s)
        else:
            num = self.dfs(i+1,s)

        
        self.memo[s[i:]] = num 
        return num 
        
            