#network2
from importlib.resources import path
from tkinter import Y
import networkx as nx
import json
import os
import matplotlib.pyplot as plt

G = nx.Graph()
i = 0
lista = []
#for everyfile in folder:
    #openfile
    #for everyfollower in file:
        #network.x add edge to user id.
    #closefile'
path = "E:/Projekteja&koodeja/SNA/sna/fakenewsnet_dataset_sample/politifact/fake"
i = 1
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith('.json'): 
            list_of_files[filename] = os.sep.join([dirpath, filename])
            
    # checking if it is a file
            if os.path.isfile(list_of_files[filename]):
                with open(list_of_files[filename]) as file:
                    data = json.load(file)
                    try:
                        id = data["user"]
                        id = id["id"]
                    except KeyError:
                        pass
                    if id not in lista:
                        i = i+1
                        lista.append(id)
                        G.add_node(id)
print(lista)
dir = 'E:/Projekteja&koodeja/SNA/sna/fakenewsnet_dataset_sample/user_followers'
for filename in os.listdir(dir):
    s = os.path.join(dir, filename)
    if os.path.isfile(s):
        with open(s) as file:
            data = json.load(file)
            id = data["user_id"]
            if id in lista:
                for state in data["followers"]:
                    if (state in lista) and (id in lista) :
                        G.add_edge(state, id)
print(G)
remove = [node for node,degree in dict(G.degree()).items() if degree == 0]
G.remove_nodes_from(remove)
print(G)
centerality = nx.degree_centrality(G)
new_output = list(centerality.values())
x = 0
y = 0
for number in new_output:
    x = x + number
    y = y + 1
avg_centr = x/y 
print("This is avg. degree centrality ")
print(avg_centr)
clustering = nx.clustering(G)
new_output = list(clustering.values())
x = 0
y = 0
for number in new_output:
    x = x + number
    y = y + 1
avg_centr = x/y 
print("This is clustering coefficient: ")
print(avg_centr)
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])
print("This is the largest component: ")
print(G0)
diameter = nx.diameter(G0)
print("This is diameter: ")
print(diameter)

nx.draw_networkx(G, with_labels=False)
plt.show()

#print("here")
#plt.savefig("biggraph.pdf")