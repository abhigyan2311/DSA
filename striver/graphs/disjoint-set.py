n = 5

rank = [0] * n
parent = [i for i in range(n)]

def findParent(node):
    if node == parent[node]:
        return node
    parent[node] = findParent(parent[node])

def union(u, v):
    u = findParent(u)
    v = findParent(v)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1

