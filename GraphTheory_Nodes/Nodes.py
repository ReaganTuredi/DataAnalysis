import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'),('B','C'),('B','D'),('C','D')])
val_map = {'A': 100,'D': 1.0,'B': 1.0}
values = [val_map.get(node, 1) for node in G.nodes()]
nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True)
plt.show()

nx.circular_layout(G)

pos_dodecahedron = {0: (1.1888206453689418, 0.38627124296868426), 1: (7.654042494670958e-17, 1.25), 2: (-1.1888206453689418, 0.38627124296868437), 3: (-0.7347315653655916, -1.011271242968684), 4: (0.7347315653655911, -1.0112712429686845), 5: (0.7132923872213651, 0.23176274578121053), 6: (4.592425496802574e-17, 0.75), 7: (-0.7132923872213651, 0.23176274578121064), 8: (-0.4408389392193549, -0.6067627457812105), 9: (0.4408389392193547, -0.6067627457812107), 10: (-0.4755282581475768, -0.15450849718747364), 11: (-9.184850993605148e-17, -0.5), 12: (0.47552825814757677, -0.1545084971874738), 13: (0.2938926261462367, 0.4045084971874736), 14: (-0.29389262614623646, 0.40450849718747384), 15: (-0.2377641290737884, -0.07725424859373682), 16: (-4.592425496802574e-17, -0.25), 17: (0.23776412907378838, -0.0772542485937369), 18: (0.14694631307311834, 0.2022542485937368), 19: (-0.14694631307311823, 0.20225424859373692)}

nodes_dodecahedron = pos_dodecahedron.keys()
edges_dodecahedron = [(0,1), (1,2), (2,3), (3,4), (4,0),
                     (0,5), (1,6), (2,7), (3,8), (4,9),
                     (6,14), (14,7), (7,10), (10,8), (8,11),
                     (11,9), (9,12), (12,5), (5,13), (13,6),
                     (10,15), (11,16), (12,17), (13,18), (14,19),
                     (15,16), (16,17), (17,18), (18,19), (19,15)]

dodecahedron = nx.Graph()
#add nodes from a nodelist
dodecahedron.add_nodes_from(nodes_dodecahedron)
# add edges from an edgelist
dodecahedron.add_edges_from(edges_dodecahedron)

pos1 = nx.layout.circular_layout(dodecahedron)
pos2 = nx.layout.spectral_layout(dodecahedron)
pos3 = nx.layout.kamada_kawai_layout(dodecahedron)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
nx.draw(dodecahedron, pos=pos1, ax=ax[0,0])
nx.draw(dodecahedron, pos=pos2, ax=ax[0,1])
nx.draw(dodecahedron, pos=pos3, ax=ax[1,0])
nx.draw(dodecahedron, pos=pos_dodecahedron, ax=ax[1,1])

pos_dodecahedron = {0: (1.1888206453689418, 0.38627124296868426), 1: (7.654042494670958e-17, 1.25), 2: (-1.1888206453689418, 0.38627124296868437), 3: (-0.7347315653655916, -1.011271242968684), 4: (0.7347315653655911, -1.0112712429686845), 5: (0.7132923872213651, 0.23176274578121053), 6: (4.592425496802574e-17, 0.75), 7: (-0.7132923872213651, 0.23176274578121064), 8: (-0.4408389392193549, -0.6067627457812105), 9: (0.4408389392193547, -0.6067627457812107), 10: (-0.4755282581475768, -0.15450849718747364), 11: (-9.184850993605148e-17, -0.5), 12: (0.47552825814757677, -0.1545084971874738), 13: (0.2938926261462367, 0.4045084971874736), 14: (-0.29389262614623646, 0.40450849718747384), 15: (-0.2377641290737884, -0.07725424859373682), 16: (-4.592425496802574e-17, -0.25), 17: (0.23776412907378838, -0.0772542485937369), 18: (0.14694631307311834, 0.2022542485937368), 19: (-0.14694631307311823, 0.20225424859373692)}

nodes_dodecahedron = pos_dodecahedron.keys()
edges_dodecahedron = [(0,1), (1,2), (2,3), (3,4), (4,0),
                     (0,5), (1,6), (2,7), (3,8), (4,9),
                     (6,14), (14,7), (7,10), (10,8), (8,11),
                     (11,9), (9,12), (12,5), (5,13), (13,6),
                     (10,15), (11,16), (12,17), (13,18), (14,19),
                     (15,16), (16,17), (17,18), (18,19), (19,15)]

dodecahedron = nx.Graph()
#add nodes from a nodelist
dodecahedron.add_nodes_from(nodes_dodecahedron)
# add edges from an edgelist
dodecahedron.add_edges_from(edges_dodecahedron)

pos1 = nx.layout.circular_layout(dodecahedron)
pos2 = nx.layout.spectral_layout(dodecahedron)
pos3 = nx.layout.kamada_kawai_layout(dodecahedron)



fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
nx.draw(dodecahedron, pos=pos1,cmap=plt.get_cmap('Greys'), ax=ax[0,0],with_labels=True)
nx.draw(dodecahedron, pos=pos2,cmap=plt.get_cmap('viridis'), ax=ax[0,1],with_labels=True)
nx.draw(dodecahedron, pos=pos3,cmap=plt.get_cmap('viridis'), ax=ax[1,0],with_labels=True)
nx.draw(dodecahedron, pos=pos_dodecahedron,cmap=plt.get_cmap('viridis'), ax=ax[1,1],with_labels=True)

#drawing K5

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'),('B','C'),('B','D'),('B','E'),('C','D'),('C','E')])
val_map = {'A': 100,'D': 1.0,'B': 1.0}
values = [val_map.get(node, 1) for node in G.nodes()]
nx.draw(G, cmap=plt.get_cmap('plasma'), node_color=values, with_labels=True)
plt.show()
