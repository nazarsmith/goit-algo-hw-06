from task_1 import GraphWorkshop

nodes = {
        "A": ["LT", "H2", "CM2", "A1"],
        "A1": ["A", "A2", "H3"],
        "A2": ["A1", "S3"],
        "B": ["TH1", "TH2"],
        "T": ["M"],
        "M": ["T", "CH", "C"],
        "C": ["M", "C1", "TH2", "P"],
        "C1": ["C", "CH", "CM2"],
        "P": ["C", "LT", "P1"],
        "P1": ["P"],
        "LT": ["P", "A", "S"],
        "S": ["LT", "S1", "S2"],
        "S1": ["S", "S4", "R2"],
        "S2": ["S1", "S", "S3", "R1"],
        "S3": ["DE", "A2", "S2"],
        "S4": ["S1", "I"],
        "R1": ["CR", "R2", "S2"],
        "R2": ["S1", "R1"],
        "H1": ["CM", "H2"],
        "H2": ["H1", "A"],
        "H3": ["A1"],
        "DE":["S3"],
        "I": ["TH2", "S4"],
        "TH1": ["B", "M"],
        "TH2": ["B", "TH1", "I"],
        "CM1": ["CH", "CM2"],
        "CM2": ["CM1", "A", "C1", "RD", "H1"],
        "RD": ["CM2"],
        "CR": [],
        "CH": ["M", "CM1"]
    }

graph_workshop = GraphWorkshop(nodes)

## Task 1
graph_workshop.construct_undirected_graph()
un_graph = graph_workshop.un_G
graph_workshop.draw_graph(un_graph)
un_graph_props = graph_workshop.get_graph_properties(un_graph)
nodes, graph = graph_workshop.aggregate_properties(un_graph, un_graph_props)

## Task 2
bfs_tree_edges = list(graph_workshop.bfs(un_graph, "LT").edges())
dfs_tree_edges = list(graph_workshop.dfs(un_graph, "LT").edges())

print("\nTask 2:\n")
print("BFS results:", bfs_tree_edges)
print("DFS results:", dfs_tree_edges)

graph_workshop.draw_dbfs_tree(bfs_tree_edges)
graph_workshop.draw_dbfs_tree(dfs_tree_edges)

## Task 3
print("\nTask 3:\n")
leafs = un_graph_props["leaf_nodes"]
print(leafs)
for i in range(len(leafs) - 1):
    print(
        f"Shortest path from {leafs[i]} to {leafs[i + 1]}:",
        graph_workshop.dij(
            graph = un_graph, source = leafs[i], target = leafs[i + 1]
        )
    )