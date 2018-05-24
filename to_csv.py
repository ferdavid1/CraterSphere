import csv
from dbfread import DBF

with open('Data.csv', 'w') as csvfile:
	table = DBF('RobbinsCraterDatabase_20120821_LatLonDiam.dbf')
	writer = csv.writer(csvfile, delimiter=',')

	writer.writerow(table.field_names)
	for record in table:
	    writer.writerow(list(record.values()))