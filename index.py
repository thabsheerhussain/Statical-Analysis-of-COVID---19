import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as mt

g = nx.read_edgelist('dataset.txt') 

print(nx.info(g))

nx.draw(g)

plt.show()