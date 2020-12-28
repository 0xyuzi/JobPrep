import math
from scipy.stats import norm
class Solution:
    def n_game(self, m,n,k):
        """
        naive dp, LTE when n, m, k = 1000,1000,1000 
        m: maximum blood reduction in each turn
        k: num of turns
        n: the total blood points

        """
        # all of failure the the max points in k turn cannot be get higher than n reduction 
        if m*k < n:
            return 0.0
        
        if m*k/n > 50:
            return 1.0
        
        # dp [i,j], in ith turn, to get the accumulate point j,  n, m, k = 35,7,7
        dp = [[0.0]*(n+1) for i in range(k)]

        # initialization
        for i in range(m+1):
            dp[0][i] = 1/(m+1)

        for i in range(1, k):
            for j in range(n+1):
                for p in range(m+1):
                    if  j - p >= 0:
                        dp[i][j] += dp[i-1][j-p]/(m+1)
        
        # self.prnt(dp)
        res = 0
        for i in range(n):
            res += dp[k-1][i]
        return 1- res

    def prnt(self,dp):
        print("----------------")
        for row in dp:
            print(row)
        
        print("----------------")

    def n_game_approx(self, m,n,k):
        """
        Approximate method by using central limit theory
        reference: https://ocw.aprende.org/courses/physics/8-044-statistical-physics-i-spring-2013/readings-notes-slides/MIT8_044S13_ProbabilityCh4.pdf
        analytical solution reference (not sure how to apply the gamma and the summation term) https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/Chapter7.pdf
        
        """
        sample_mean = 0.5*m
        sample_var = ((m+1)**2-1)/12

        cum_prob = 0
        test_prob = 0
        for i in range(n):
            cum_prob += 1/math.sqrt(2*math.pi*k*sample_var) * math.exp(-0.5*(i - k*sample_mean)**2/(k*sample_var))
            test_prob += norm.pdf(i, k*sample_mean, math.sqrt(k*sample_var))
            
        
        print(f"scipy norm function results: {1 - test_prob}")
        return 1- cum_prob
        

if __name__ == "__main__":
    sol = Solution()
    n, m, k = 1000,1000,1000

    print(sol.n_game(m,n,k))
    print(sol.n_game_approx(m,n,k))



