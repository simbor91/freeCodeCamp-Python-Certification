# Graphs and Trees
# 030 Lab: Build an Adjacency List to Matrix Converter

def adjacency_list_to_matrix(adj_list):
    # 1. Determine the number of nodes
    # The number of nodes corresponds to the number of keys in the dictionary
    num_nodes = len(adj_list)
    
    # 2. Initialize the matrix with zeros
    # We create a square matrix of size num_nodes x num_nodes
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    # 3. Populate the matrix
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            # Set the entry at [node][neighbor] to 1 to represent an edge
            matrix[node][neighbor] = 1
            
    # 4. Print each row in the matrix
    for row in matrix:
        print(row)
        
    # 5. Return the adjacency matrix
    return matrix

adj_list = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
adjacency_list_to_matrix(adj_list)