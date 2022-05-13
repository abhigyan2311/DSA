import math
 
def combb(n, r):
    res = 1
    for i in range(1, r+1):
        res *= (n-r+i)/(i)
        # print(res)
    return round(res)
 
# driver code
print(combb(5, 4))