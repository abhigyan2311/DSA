from math import comb, factorial

print(comb(5-1, 3-1))

# def nCr(n, r):
#     f = factorial
#     return f(n)//(f(r)*f(n-r))

# print(nCr(5-1,3-1))


row = 5
ans = [1]
prev = 1
for col in range(1, row+1):
    prev *= row - col + 1
    prev //= col
    ans.append(prev)
print(ans)