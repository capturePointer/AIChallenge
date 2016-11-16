from scipy.stats import kurtosis, skew, entropy
from sklearn import svm, tree
from audio_processing import get_file_attributes
import pyaudio
import wave
import numpy as np
import csv
import math

x_vars = []
y_vars = []

def read_data():
	with open('voice.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			row_list = row[0].strip(" \"")
			row_list = row_list.replace("\"" , "")
			row_list = row_list.split(",")
			x_vars.append(np.array(row_list[:len(row_list) - 1]))
			gender = str(row_list[len(row_list) - 1])
			if gender == "male":
				y_vars.append(0)
			elif gender == "female":
				y_vars.append(1)

read_data()

x_vars = x_vars[1:]
x_vars = np.array(x_vars)
y_vars = np.array(y_vars)
print(x_vars)
print(y_vars)

#clf = svm.SVC()
clf = tree.DecisionTreeClassifier()
clf.fit(x_vars, y_vars)

print(clf.predict([[0.0597809849598081,0.0642412677031359,0.032026913372582,0.0150714886459209,0.0901934398654331,0.0751219512195122,12.8634618371626,274.402905502067,0.893369416700807,0.491917766397811,0,0.0597809849598081,0.084279106440321,0.0157016683022571,0.275862068965517,0.0078125,0.0078125,0.0078125,0,0]]))
print(clf.predict([[0.165508946001837,0.0928835369116316,0.183043922369765,0.0700715015321757,0.250827374872319,0.180755873340143,1.70502911922022,5.76911536636857,0.938829422236203,0.601528810198165,0.267701736465781,0.165508946001837,0.185606931233589,0.0622568093385214,0.271186440677966,0.227022058823529,0.0078125,0.5546875,0.546875, 0.035]]))

song_attributes = get_file_attributes("lana.wav")
print(song_attributes)
print(clf.predict([song_attributes]))

song_attributes = get_file_attributes("woman_voice.wav")
print(song_attributes)
print(clf.predict([song_attributes]))

song_attributes = get_file_attributes("audio.wav")
print(song_attributes)
print(clf.predict([song_attributes]))







