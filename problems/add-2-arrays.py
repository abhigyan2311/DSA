# https://youtu.be/Z7_nMTHROZo

from typing import List

def add2Arrays(a: List[int], b: List[int]) -> int:
    #Approach 1: Simple trick :D
    # a= int("".join(map(str, a)))
    # b= int("".join(map(str, b)))
    # sum = a+b
    # return [int (d) for d in str(sum)]

    #Approach 2: Array Traversal
    i = len(a)-1
    j = len(b)-1
    carry = 0
    ans = []
    while i >= 0 and j >= 0:
        v1,v2 = a[i], b[j]
        sum = v1 + v2 + carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)
        i -= 1
        j -= 1

    while i>=0:
        sum = a[i] + carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)
        i -= 1

    while j>=0:
        sum = a[j] + carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)
        j -= 1
    
    while carry != 0:
        sum = carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)

    ans.reverse()
    return ans


ans = add2Arrays([1,2,5], [4,5,6])
print(ans)