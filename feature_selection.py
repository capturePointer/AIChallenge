from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import csv


boston = load_boston()


x_vars = []
y_vars = []

with open('voice.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		#print ', '.join(row)
		row_list = row[0].strip(" \"")
		row_list = row_list.replace("\"" , "")
		row_list = row_list.split(",")
		x_vars.append(row_list[:len(row_list) - 1])
		#print(row_list[len(row_list) - 1])
		gender = str(row_list[len(row_list) - 1])
		#print(gender)
		if gender == "male":
			#print("male")
			y_vars.append(0)
		elif gender == "female":
			#print("female")
			y_vars.append(1)

names = x_vars[0]
x_vars = x_vars[1:]
X = x_vars
Y = y_vars

rf = RandomForestRegressor()
rf.fit(X, Y)
print "Features sorted by their score:"
print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), 
             reverse=True)
"""
[(0.8581, 'meanfun'), (0.0587, 'IQR'), (0.0135, 'sfm'), (0.0133, 'minfun'), (0.0056, 'Q75'), 
(0.0055, 'skew'), (0.0049, 'sp.ent'), (0.0044, 'dfrange'), (0.004, 'mode'), (0.004, 'kurt'), 
(0.0038, 'sd'), (0.0038, 'Q25'), (0.0034, 'modindx'), (0.0031, 'meandom'), (0.0028, 'maxfun'), 
(0.0024, 'mindom'), (0.0023, 'maxdom'), (0.0023, 'centroid'), (0.002, 'median'), (0.0017, 'meanfreq')]
"""
