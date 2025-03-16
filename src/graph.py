import networkx as nx
import matplotlib.pyplot as plt
# 1
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G
# 2
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree(node)
# 3
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G, source=start))
# 4
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, source=start))
# 5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source=source, target=target)
# 6
def visualize_graph(G: nx.Graph, filename: str = "graf.png") -> None:
    plt.figure()
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    plt.savefig(filename)
    plt.close()
