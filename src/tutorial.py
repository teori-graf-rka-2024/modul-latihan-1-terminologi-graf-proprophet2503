from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

# 1. Create Graph
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5), (2, 6), (3, 6), (4,6), (5,6), (1,6)]

G = create_graph(edges)
print(G)
# 2. Get degree
node = 2
print(get_degree(G, node))

# 3.  DFS traversal
start_node = 1
print(dfs_traversal(G, start_node))

# 4. BFS traversal
print(bfs_traversal(G, start_node))

# 5. Find shortest path 
print(find_shortest_path(G, 1, 3))

# 6 VIsualize Graph
visualize_graph(G)

