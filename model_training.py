from scipy.stats import kurtosis, skew, entropy
from sklearn import svm, tree
from audio_processing import get_file_attributes
import pyaudio
import wave
import numpy as np
import csv
import math
import cPickle

def read_data(training_data):
	with open(training_data, 'rb') as csvfile:
		variables = {}
		x_vars = []
		y_vars = []
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
		x_vars = x_vars[1:]
		x_vars = np.array(x_vars)
		y_vars = np.array(y_vars)
		variables['x_vars'] = x_vars
		variables['y_vars'] = y_vars
		return variables

def train_model(variables):
	clf = tree.DecisionTreeClassifier()
	clf.fit(variables['x_vars'], variables['y_vars'])
	return clf

if __name__ == "__main__":
	variables = read_data('voice.csv')
	clf = train_model(variables)
	with open('voice_recognition.pkl', 'wb') as fid:
		cPickle.dump(clf, fid)






