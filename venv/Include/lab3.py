import math
import random
import networkx as nx
import matplotlib.pyplot as plt



inf = math.inf
n=int(input("Please enter number of nodes"))
v=int(input("Start node`s index"))
v_end = int(input("Final node`s index"))
d = [ inf for i in range(n)]
d[v]=0
e = [{"first":0,"second":1,"value":2},{"first":1,"second":2,"value":3},{"first":2,"second":3,"value":1},
     {"first":1,"second":3,"value":2},{"first":3,"second":4,"value":5},{"first":4,"second":5,"value":4},
     {"first":5,"second":6,"value":1},{"first":6,"second":1,"value":2}]

g = nx.Graph()
nodes = nx.path_graph(7)
g.add_nodes_from(nodes)

    
    
for i in range(n):
     for j in range(len(e)):
        if d[e[j]["second"]]>d[e[j]["first"]]+e[j]["value"]:
            d[e[j]["second"]] = d[e[j]["first"]]+e[j]["value"]
        if d[e[j]["first"]]>d[e[j]["second"]]+e[j]["value"]:
            d[e[j]["first"]] = d[e[j]["second"]]+e[j]["value"]
print(e)
print(d)
first_edges_list=[]
#[{"first":random.randint(0,n-1),"second":random.randint(0,n-1),"value":random.randint(0,n-1)} for i in range(n)]
g = nx.Graph()
nodes = nx.path_graph(7)
g.add_nodes_from(nodes)
for i in e:
    g.add_edge(i["first"],i["second"],color="r",weight=i["value"])
    first_edges_list.append((i["first"],i["second"]))
my_path = nx.bellman_ford_path(g, v, v_end)
print(my_path)
my_final_path =[(my_path[i],my_path[i+1]) for i in range(len(my_path)) if i <len(my_path)-1]
print(my_final_path)
g.remove_edges_from(my_final_path)
#for i in my_final_path:
#    g.add_edge(i[0],i[1],color="g")
pos = nx.circular_layout(g)
first_edges_list = list(set(first_edges_list)-set(my_final_path))
nx.draw_networkx_nodes(g,pos,nodelist=nodes)
nx.draw_networkx_edges(g,pos,edgelist=first_edges_list,edge_color="r")
nx.draw_networkx_edges(g,pos,edgelist=my_final_path,edge_color="g")
labels = {}
labels[0] = r'$0$'
labels[1] = r'$1$'
labels[2] = r'$2$'
labels[3] = r'$3$'
labels[4] = r'$4$'
labels[5] = r'$5$'
labels[6] = r'$6$'
nx.draw_networkx_labels(g, pos, labels, font_size=16)
plt.axis("off")
plt.show()