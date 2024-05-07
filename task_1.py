import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

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

fig = plt.figure(figsize = (11,11))

G = nx.Graph()

for k,v in nodes.items():
    [G.add_edge(k, node, weight = len(v) / 2) for node in v]

pos = nx.kamada_kawai_layout(G)
edges = G.edges()
nodes = G.nodes()

weights = [G[u][v]['weight'] for u,v in edges]

nx.draw(G, pos = pos, with_labels = True, width = weights)
closensess = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

nodes_properties = {}
for n in nodes:
    nodes_properties.update(
        {
            n: {
                "degree_centrality": G.degree(n),
                "closeness_centrality": closensess[n],
                "betweenness_centrality": betweenness[n],
            }
        }
    )
n_props = pd.DataFrame.from_dict(nodes_properties)

graph_properties = {
    "G" : {
        "Number of nodes": len(nodes),
        "Number of edges:": len(edges),
        "Graph is connected": nx.is_connected(G),
        "Average node degree": n_props.loc["degree_centrality"].mean()
    }
}
g_props = pd.DataFrame.from_dict(graph_properties)

plt.show()

