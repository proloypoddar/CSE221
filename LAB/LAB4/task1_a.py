def create_adjacency_matrix(n, m, edges):
    matrix = [[0] * n for _ in range(n)]

    for edge in edges:
        u, v, w = edge
        matrix[u - 1][v - 1] = w 

    return matrix

def print_adjacency_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    adjacency_matrix = create_adjacency_matrix(N, M, edges)
    print_adjacency_matrix(adjacency_matrix)

main()
