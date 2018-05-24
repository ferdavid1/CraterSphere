import pandas as pd 
import numpy as np 
import networkx
data = pd.read_csv("Data.csv")
data = data[['LON_E', 'LAT', 'DiamKM']]
lon, lat, diam = data['LON_E'], data['LAT'], data['DiamKM']



if __name__ == '__main__':
	main()