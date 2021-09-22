"""
给一个等概率的二进制随机数生成器，求[1,2,3,4,5]的均匀分布抽样器
random.randint(0, 1)
5 = (101)_2

"""
from collections import Counter
import random 


def gen(n):
    # get number of bit for n
    k = 0
    num = n 
    while num:
        k+= 1 
        num >>=1
    
    # print(f"num bits: {k}")

    res = 0
    for i in range(k):
            bit = random.randint(0, 1)
            # print(f"bit {bit}")
            res |= (bit<<i)
    
    # check the results,if not gen res meet requirement
    while res >= n:
        res = 0
        for i in range(k):
            bit = random.randint(0, 1)
            # print(f"bit {bit}")
            res |= (bit<<i)

        

    return res 

# test 
res = []
for i in range(1000000):
    res.append(gen(5)+1)


counter = Counter(res)
print(counter)
 
