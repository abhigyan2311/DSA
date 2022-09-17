n = 5

rank = [0] * n
parent = [i for i in range(n)]

# TC - 4α if using path compression


def findParent(node):
    if parent[node] != node:
        parent[node] = findParent(parent[node])  # Path Compression
    return parent[node]


def union(u, v):
    u = findParent(u)
    v = findParent(v)
    if rank(u) < rank(v):
        parent[u] = v
    elif rank(u) > rank(v):
        parent[v] = u
    else:
        parent[u] = v
        rank[v] += 1
