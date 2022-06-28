# [2, 4, 5, 16, 25]

# O(N2logN) + O(NlogN)
def maxSetSize(riceBags):
    # Write your code here
    maxLen = 0
    riceBags.sort()
    n = len(riceBags)
    visited = set()
    i = 0
    while i < n:
        curr = riceBags[i]
        if curr in visited:
            i += 1
            continue
        currLen = 1
        visited.add(curr)
        target = curr*curr
        j = i+1
        while j < n:
            curr = riceBags[j]
            if curr == target:
                currLen += 1
                j += 1
                target = curr*curr
                visited.add(curr)
            else:
                if riceBags[j] > target: break
                j += 1
        i += 1
        maxLen = max(maxLen, currLen)
    return maxLen

ans = maxSetSize([2,4,5,16,25,256,125, 3, 9, 81, 6561, 43046721])
print(ans)