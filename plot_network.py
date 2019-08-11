import sys
sys.path.append('')

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from fa2 import ForceAtlas2
from sklearn.cluster import SpectralClustering
from curved_edges_numba import curved_edges
import pandas as pd

# Number of clusters
n = 4
loop_list = list(range(0,n))

colors = ['#FF3333','#FF9333','#33FF36','#33FFC7','#33F3FF','#33A8FF','#F333FF','#FF3361']
colors = colors[:n]

# Importing network as Pandas dataframe
network = pd.read_csv(r'',sep=" ",header=None, names=['from','to'])

# Creating initial graph
G = nx.from_pandas_edgelist(network,'from','to',create_using=nx.Graph())

print('Clustering...','\n')
# Performing spectral clustering
matrix = nx.to_numpy_matrix(G)
sc = SpectralClustering(n, affinity='precomputed', n_init=100,assign_labels='discretize')
sc.fit(matrix)
clusters = pd.DataFrame({'group':sc.labels_})

# Rearraging graph for coloring
#clusters = clusters.reindex(G.nodes())

print('Force Atlas...','\n')
# Running Force Atlas
forceatlas2 = ForceAtlas2()
positions = forceatlas2.forceatlas2_networkx_layout(G,pos=None,iterations=100)

print('\n','Curves...','\n')
lc_dict = {}
for n, c in zip(loop_list,colors):
# Making a new network based on selected cluster
    network_sub = pd.merge(network,clusters[clusters['group'] == n],left_on='to',right_index=True,how='inner').drop(['group'],axis=1).reset_index(drop=True)
    
    # Making a list that has the nodes we want to keep
    node_list = set(list(dict.fromkeys(network_sub['to'].tolist() + network_sub['from'].tolist())))
    
    # Getting the subset of the atlast positions dict
    positions_sub = {k:v for k, v in positions.items() if k in node_list}
    
    # Loading a new network based on the subset
    G_sub = nx.from_pandas_edgelist(network_sub,'from','to',create_using=nx.Graph())
    print(G_sub.number_of_nodes())
    
    curves = curved_edges(G_sub,positions_sub)
    lc = LineCollection(curves,color=c,alpha=.05)
    
    lc_dict[n] = lc
    
# Plot
print('\n','Plotting...')
def plot():
    plt.figure(figsize=(10,10))
    plt.gca().set_facecolor('k')
    for key,value in lc_dict.items():
        plt.gca().add_collection(lc_dict[key])
    plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
    plt.axis('tight')
    plt.savefig(r'',format='png',dpi=100)
    plt.show()
plot()