import networkx as nx
from networkx.algorithms import isomorphism


vertices_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges_list_1 = [(1, 9), (2, 9), (3, 9), (3, 10), (4, 8), (5, 8), (5, 10), (6, 9), (7, 8)]

vertices_list_2 = [8, 20, 22, 25, 32, 39, 51, 71, 81, 88]
edges_list_2 = [(8, 20), (20, 32), (20, 81), (22, 51), (25, 39), (25, 51), (39, 81), (51, 71), (51, 88)]

G1 = nx.Graph()
G1.add_nodes_from(vertices_list_1)
G1.add_edges_from(edges_list_1)

G2 = nx.Graph()
G2.add_nodes_from(vertices_list_2)
G2.add_edges_from(edges_list_2)

# Obtain the isomorphism mapping
gm = nx.isomorphism.GraphMatcher(G1, G2)
is_isomorphic = gm.is_isomorphic()
mapping = gm.mapping

# Print the isomorphism mapping in the order of vertex_set_list_1
if is_isomorphic:
    print("The graphs are isomorphic.")
    print("Isomorphism mapping:")
    for node in vertices_list_1:
        mapped_node = mapping.get(node)
        if mapped_node is not None:
            print(f"graph1: {node} -> graph2: {mapped_node}")
else:
    print("The graphs are not isomorphic.")