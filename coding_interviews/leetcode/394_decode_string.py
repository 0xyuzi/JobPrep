class Solution:
    def decodeString(self, s: str) -> str:
        
        result = self.dfs(s,0)
        
        return result
        
    
    
    def dfs(self, s, i):
        res = ''
        rep_num = 0
        
        while i<len(s):
            
            if '0'<= s[i] <='9':
                rep_num = rep_num*10 + int(s[i])
                
            elif s[i] == '[':
                i, sub_str = self.dfs(s, i+1)
                # print(f"rep_num: {rep_num}, sub_str: {sub_str}")
                res += rep_num*sub_str
                rep_num = 0
                # print(res)
            elif s[i] == ']':
                # print(res, i)
                return  i,res 
            else:
                res += s[i]
            
            i += 1
        return res
                
            
            