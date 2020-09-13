
"""
@param m: An integer m denotes the size of a backpack
@param A: Given n items with size A[i]
@return: The maximum size
"""
def backPack(self, m, A):
    # write your code here
    
    # dp[i][j] -> the max size to fill in the backpack which has size j when go over to the ith backpack 
    # time complexity: O(mn), space complexity O(mn),n is the len(A)    
    # initialization
    dp = [[0]*(m + 1) for _ in range(len(A)+1)]
    print(len(dp),len(dp[0]))
    
    for i in range(1,len(A)+1):
        for j in range(1, m+1):
            print(i)
            if j > A[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] +A[i-1])
            else:
                    dp[i][j] = dp[i-1][j]
    
    return dp[len(A)][m]
    
    
    

def backPack(self, m, A):
    # write your code here
    # reduce the space complexity to O(m)
    
    # dp[i][j] -> the max size to fill in the backpack which has size j when go over to the ith backpack 
    
    # initialization
    dp = [0]*(m + 1)
    # print(len(dp),len(dp[0]))
    
    for size in A:
        for j in range(m, size-1,-1):
            
            dp[j] = max(dp[j], dp[j-size]+size)
            
    
    return dp