# ColorfulNetworkX
| <img src="https://github.com/nbucklin/ColorfulNetworkX/blob/master/facebook_combined.png" height=400px> | 
|---|

This program draws NetworkX networks with groups colored based on spectral clustering. Also used are bezier curves to created curved edges instead of straight ones. I heavily leverage the work done by [BeyondBeneath](https://github.com/beyondbeneath) [here](https://github.com/beyondbeneath/bezier-curved-edges-networkx). While I chose to use spectral clustering as the community detection method, other approaches could be used with this framework. ForceAtlas2 is used for the layout algorithm. 

### Usage
Make sure that `curved_edges.py` is in the same folder as `draw_network.py`.  

Alter the number of communities you would like to identify:
```
# Number of clusters
n = 4
```

### Example
Below is an example of a network created from the `facebook_combined` dataset available at [SNAP](https://snap.stanford.edu/data/egonets-Facebook.html).
![Image](https://github.com/nbucklin/ColorfulNetworkX/blob/master/facebook_combined.png)
