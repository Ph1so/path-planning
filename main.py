import json
import copy

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

import osmnx as ox
from IPython.display import HTML

ox.settings.use_cache = True
ox.settings.cache_folder = './cache' 

address = "Cary Memorial Library, 1874 Massachusetts Ave, Lexington, MA 02420"

try:
    G = ox.graph_from_address(address, dist=800, network_type="walk")
    start_node = ox.distance.nearest_nodes(G, X=-71.2299, Y=42.4479)
    print(start_node)
    end_node = ox.distance.nearest_nodes(G, X=-71.2328, Y=42.4429)
    print(end_node)
    node_colors = ['red' if node == start_node else 'green' if node == end_node else 'white' for node in G.nodes()]
    node_sizes = [100 if node == start_node or node == end_node  else 15 for node in G.nodes()]

    adj_dict = {
        str(u): {str(v): d[0]['length'] for v, d in nbrs.items()}
        for u, nbrs in G.adj.items()
    }
    fig, ax = ox.plot_graph(
        G, 
        node_color=node_colors, 
        node_size=node_sizes, 
        node_zorder=3, 
        bgcolor='black'
    )
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")