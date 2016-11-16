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

