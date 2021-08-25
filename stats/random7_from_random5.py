"""
create random 7 from random 5 function 
https://ask.julyedu.com/detail/?id=98577

https://blog.csdn.net/jiyanfeng1/article/details/43526247


"""
import random 

def gen_random5():
    return random.randint(1,5)

def gen_random7():
    num = (gen_random5() - 1) *5 + gen_random5() 
    while num > 21:
        num = (gen_random5() - 1) *5 + gen_random5()
    
    return num%7+1

# test this function

res = []
for _ in range(100000):
    res.append(gen_random7())

print(res)

for i in range(1,8):
    print(f" gen {i} prob: {res.count(i)/len(res)}")


