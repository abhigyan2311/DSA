
def fibb(n):
    if n <= 1:
        return n
    return fibb(n-1) + fibb(n-2)

ans = fibb(10)
print(ans)