import pandas as pd 
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 

eps = 1
def neighborhood_dist(lat1, lon1, lat2, lon2, eps=eps):
	dist = np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
	return dist < eps 

def main():
	data = pd.read_csv("Data.csv")
	data = data[['LON_E', 'LAT', 'DiamKM']][:5000]
	lon, lat, diam = data['LON_E'], data['LAT'], data['DiamKM']
	G = nx.MultiGraph()
	zipped = list(zip(lat, lon))
	G.add_nodes_from(zipped)
	inds = []
	for ind, (x,y) in enumerate(zipped):
		for x2,y2 in zipped:
			if neighborhood_dist(x,y,x2,y2) and (x,y) != (x2,y2):
				G.add_edge((x,y), (x2,y2))
				inds.append(ind)
			else:
				pass
	diam = [diam[ind] for ind in inds]
	# print(len(list(G.edges())))
	nx.draw(G, node_size=diam, with_labels=False)
	plt.show()

main()