"""
Question:

Given an array of integers nums and integer k, return the total number of continuous subarrays whose sum equals to k.
nums = [1,-2,1,2,1,1] k =3

nums = [1,-2,1,2,1,1] k = 3

nums[i:j]

"""
def sub_array_sum(nums, k):
    n = len(nums)

    res = 0
    for i in range(n-1):
        cum_sum = nums[i]
        for j in range(i+1,n):
            cum_sum += nums[j]
            if cum_sum == k:
                print(f"find k in subarray{i,j} ")
                res += 1 
    
    return res 


nums =  [1,-2,1,2,1,1]
k = 3

print(sub_array_sum(nums,k))
            


