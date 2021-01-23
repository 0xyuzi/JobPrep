from bisect import bisect
def job_schdule(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key = lambda v:v[1])
    print(jobs)
    # endtime, max profit
    dp = [[0, 0]]

    for s, e, p in jobs:
        i = bisect(dp, [s+1]) - 1 
        print(s,e,p)
        print(f"find the index of max profit in {i}")
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
        
        print(dp)
        
    return dp[-1][1]