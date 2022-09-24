class Solution:
    def shortest_distance(self, matrix):
        # Prepare adjacency matrix with -1 if edge doesnt exist
        # Initialize the solution matrix same as the input graph matrix as a first step.
        # Then update the solution matrix by considering all vertices as an intermediate vertex.
        # The idea is to one by one pick all vertices and updates all shortest paths which include the picked vertex as an intermediate vertex in the shortest path.
        # When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices.
        # For every pair (i, j) of the source and destination vertices respectively, there are two possible cases.
        # k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
        # k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]

        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] != -1 and matrix[k][j] != -1:
                        if matrix[i][j] == -1:
                            matrix[i][j] = matrix[i][k] + matrix[k][j]
                        else:
                            matrix[i][j] = min(
                                matrix[i][j], matrix[i][k] + matrix[k][j])
        return matrix
