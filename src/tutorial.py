from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# 1. Create Graph
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5), (2, 6), (3, 6), (4,6), (5,6), (1,6)]

G = create_graph(edges)

# 2. Get degree
node = 2
print(f"Degree of node {node}: {get_degree(G, node)}")

# 3.  DFS traversal
start_node = 1
print(f"DFS Traversal from node {start_node}: {dfs_traversal(G, start_node)}")

# 4. BFS traversal
print(f"BFS Traversal from node {start_node}: {bfs_traversal(G, start_node)}")

# 5. Find shortest path 
print(f"Shortest path from 1 to 3: {find_shortest_path(G, 1, 3)}")

# 6 VIsualize Graph
visualize_graph(G)
print("Graph has been saved as 'graf.png'")
