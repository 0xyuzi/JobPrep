import math
def oom(m1,m2, faster_avaliable):
    """
    n: number of cases
    m1: size of memory 1
    m2: size of memory 2
    
    return: 
    t: number of unit time to OOM, 
    a_1: the left avaliable size of m1
    a_2 :the left avaliable size of m2
    """

    # first reduce the two memory to the similar size
    # for example len(m1) = 10^4, len(m2) = 100
   
    
    if faster_avaliable:    
        if m1 >= m2:
            diff = m1 - m2
            time = math.floor(0.5*(-1 + math.sqrt(1+8*diff))) -1 
            count = int(0.5*(time+1)*time)
            m1 -= count
        else:
            diff = m2-m1
            time = math.floor(0.5*(-1 + math.sqrt(1+8*diff))) -1 
            count = int(0.5*(time+1)*time)
            
            m2 -= count 
            print(time ,count, m1, m2)
   
    
    while ( time <=m1 or time <= m2):
        time += 1
        if m1 >= m2: 
            m1 -= time 
        else:
            m2 -= time 
        
        
        print(time, m1,m2)
       
    
    return time+1, m1, m2 

if __name__ == "__main__":
    faster_avaliable = 1
    print(oom(100000,1000,faster_avaliable))

        