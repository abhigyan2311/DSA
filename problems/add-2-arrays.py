# https://youtu.be/Z7_nMTHROZo
# https://www.codingninjas.com/codestudio/problems/sum-of-two-arrays_893186

from typing import List

def add2Arrays(a: List[int], b: List[int]) -> int:
    # Approach 1: Simple trick :D
    # a= int("".join(map(str, a)))
    # b= int("".join(map(str, b)))
    # sum = a+b
    # return [int (d) for d in str(sum)]

    # Approach 2: Array Traversal
    i = len(a)-1
    j = len(b)-1
    carry,sum = 0,0
    ans = []

    while i>=0 or j>=0:
        sum = 0
        if i>=0:
            sum += a[i]
            i -= 1
        
        if j>=0:
            sum += b[j]
            j -= 1

        sum += carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)

    if carry:
        ans.append(carry)

    ans.reverse()
    return ans


ans = add2Arrays([1,2,5], [4,5,6])
print(ans)