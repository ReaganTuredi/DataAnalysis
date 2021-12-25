
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
%matplotlib inline

#BACKGROUND: we will solve the cell tower problem. Imagine many cell towers scattered throughout a city. No two cell towers can be too close to where 
    # they interfere with one another. However, they need to be close enough so that the cell company can minimize the amount of towers needed. 

#Importing data
df = pd.read_csv('TowersVNZ476413FDC428783.csv')
point = np.array((df['latitude'],df['longitude']))
x = point[0]
y = point[1]

points = []
for i in range(len(x)):
    points.append((x[i],y[i]))
    

#plot the tower data
plt.scatter(x,y)
plt.title('tower locations')
plt.ylabel('longitude')
plt.xlabel('latitude')
plt.show()


def distance(p1,p2):
    '''Returns the distance betwen two numpy points'''
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#KNN function
def nn_graph(points):
    '''Generates an adjacency matrix based on the Nearest neighbor graph algorithm.'''
    G = dict()
    for p in range(0,len(points)):
        min_distance = np.inf;
        min_point = -1
        for n in range(0,len(points)):
            if p != n:
                d = distance(points[p], points[n])
                if d < min_distance:
                    min_distance = d
                    min_point = n
        if min_point == -1:
            print("ERROR-point not found")
        G[p] = min_point
    return G
  
  #KNN Graph
  def knn_graph(k,points):
    G = {}
    for i in range(0,len(points)):
        distances = []
        temp = []
        for j in range(0,len(points)):
            if i != j:
                d = distance(points[i], points[j])
                distances.append([d,j])
            distances.sort()
        for a in range(k):
            temp.append(distances[a][1])
        G[i] = temp
    return G
  
  # Number of locations, as a function
  def t_loc(points):
    locations = {}
    for i in range(len(points)):
        locations[i] = points[i]
    return(locations)
  
  import networkx as nx
position = t_loc(points)
edges = knn_graph(3,points)

G = nx.Graph(edges)
fig, ax = plt.subplots()

nx.draw_networkx(G, pos = position, ax = ax, with_labels = False, node_size = 40,)
plt.title('example k-nearest neighbor (k=3) graph on tower locations')
plt.ylabel('longitude')
plt.xlabel('latitude')
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
plt.show()
  
  
