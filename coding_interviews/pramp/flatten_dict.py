'''
output would be flatten dict, which on the same level 
types of values would be the same as in the original dict

'''
class Solution:
    def flatten_dictionary(self,dictionary):
        if not dictionary:
            return {}
        
        
        res = {}
        
        for k,v in dictionary.items():
            self.dfs(k, v, dictionary, res,k)
            
        
        return res

    
    
    
    def dfs(self, k,v, dictionary, res, name):
        # print(res)
        if isinstance(v, dict):
            for key,val in v.items():
                if not key:
                    self.dfs(key,val,dictionary, res, name)
                else:
                    self.dfs(key,val,dictionary, res, name+'.'+key)
        else:
            if v != None:
                res[name] = v
        return
    
    

if __name__ == "__main__":
    sol = Solution()
    
    
    # dic = {"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}
    dic = {"a":"1"}
    print(sol.flatten_dictionary(dic))