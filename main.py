import json
import copy
import math
import heapq
from dataclasses import dataclass
from typing import TypeAlias

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

import osmnx as ox
from IPython.display import HTML

ox.settings.use_cache = True
ox.settings.cache_folder = './cache' 

address = "Institute of Contemporary Art, 25 Harbor Shore Dr, Boston, MA 02210"
place = "Boston, MA"

try:
    G = ox.graph_from_address(place, dist = 2000, network_type="drive")
    start_node = ox.distance.nearest_nodes(G, X=-71.2299, Y=42.4479)
    print(start_node)
    end_node = ox.distance.nearest_nodes(G, X=-71.00328, Y=42.343929)
    print(end_node)
    node_colors = ['red' if node == start_node else 'green' if node == end_node else 'white' for node in G.nodes()]
    node_sizes = [100 if node == start_node or node == end_node  else 15 for node in G.nodes()]

    adj_dict = {
        int(u): {int(v): round(float(d[0]['length']), 2) for v, d in nbrs.items()}
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