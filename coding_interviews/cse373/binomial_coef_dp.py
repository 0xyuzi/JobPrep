def binomial_coef_dp(n,k):
    """
    implementation binomial coefficient in dynamic programming 
    """

    if n < k:
        return -1 

    dp = [ [0]*(n+1) for i in range(n+1)]

    # initialization 
    for i in range(n+1):
        dp[i][0] = 1
    # print(dp)
    for j in range(n+1):
        dp[j][j] = 1

    # dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    for i in  range(1, n+1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    print(dp)
    return dp

if __name__ == "__main__":
    res = binomial_coef_dp(5,4)

    print(res[5][4])
