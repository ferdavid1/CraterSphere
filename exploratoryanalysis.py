import pandas as pd 
import numpy as np 

data = pd.read_csv("Data.csv")
data = data[['LON_E', 'LAT', 'DiamKM']]
# print(data.head())
# print(list(map(lambda x: max(x), [data['LON_E'], data['LAT']]))) # [179.997, 85.70200000000001]
# print(list(map(lambda x: min(x), [data['LON_E'], data['LAT']]))) # [-179.997, -86.7]
# print(list(map(lambda x: np.std(x), [data['LON_E'], data['LAT']]))) # [96.64146664904727, 33.60892268513986]
# print(list(map(lambda x: np.mean(x), [data['LON_E'], data['LAT']]))) # [10.128020944833155, -7.19920876144479]


lon, lat, diam = data['LON_E'], data['LAT'], data['DiamKM']
def plot(x, title, xaxis, yaxis):
	import matplotlib.pyplot as plt 
	plt.figure()
	plt.plot(x)
	plt.title(title)
	plt.xlabel(xaxis)
	plt.ylabel(yaxis)
	plt.show()
	# plt.savefig(title + '.png')

# print(max(diam), min(diam), np.mean(diam), np.std(diam)) # 1164.22, 1.0, 3.55668639730795, 8.591981595119385
# plot(lon, 'Distribution of Crater Longitude', 'Index', 'Longitude of Crater')
# plot(lat, 'Distribution of Crater Latitude', 'Index', 'Latitude of Crater')
# plot(diam, 'Distribution of Crater Diameter', 'Index', 'Diameter of Crater')

