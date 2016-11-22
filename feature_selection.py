from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np
import csv

x_vars = []
y_vars = []

with open('voice.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		row_list = row[0].strip(" \"")
		row_list = row_list.replace("\"" , "")
		row_list = row_list.split(",")
		x_vars.append(row_list[:len(row_list) - 1])
		gender = str(row_list[len(row_list) - 1])
		if gender == "male":
			y_vars.append(0)
		elif gender == "female":
			y_vars.append(1)

names = x_vars[0]
x_vars = x_vars[1:]
X = x_vars
Y = y_vars

rf = RandomForestClassifier()
rf.fit(X, Y)

print "Features sorted by their score:"
print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), 
             reverse=True)

print(rf.predict([[0.0597809849598081,0.0642412677031359,0.032026913372582,0.0150714886459209,0.0901934398654331,0.0751219512195122,12.8634618371626,274.402905502067,0.893369416700807,0.491917766397811,0,0.0597809849598081,0.084279106440321,0.0157016683022571,0.275862068965517,0.0078125,0.0078125,0.0078125,0,0]]))
print(rf.predict([[0.165508946001837,0.0928835369116316,0.183043922369765,0.0700715015321757,0.250827374872319,0.180755873340143,1.70502911922022,5.76911536636857,0.938829422236203,0.601528810198165,0.267701736465781,0.165508946001837,0.185606931233589,0.0622568093385214,0.271186440677966,0.227022058823529,0.0078125,0.5546875,0.546875, 0.035]]))

"""
[(0.396, 'meanfun'), (0.1522, 'sd'), (0.115, 'Q25'), (0.0761, 'sfm'), (0.0642, 'IQR'), (0.0467, 'sp.ent'), 
(0.0253, 'centroid'), (0.0232, 'mode'), (0.0121, 'kurt'), (0.0112, 'meanfreq'), (0.0104, 'median'), (0.0104, 'Q75'), 
(0.01, 'meandom'), (0.0087, 'dfrange'), (0.0086, 'maxfun'), (0.0083, 'maxdom'), (0.006, 'mindom'), (0.0055, 'minfun'), 
(0.0054, 'skew'), (0.0048, 'modindx')]
"""
