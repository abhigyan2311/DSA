import math
 
def getFirstSetBitPos(n):
    rsb = math.log2(n & -n)+1
    print (f"{n} - ", rsb)
    return math.log2(n&-n)+1
 
# driver code
 
for i in range(1, 11):
    print(f"{i} - ", int(getFirstSetBitPos(i)))