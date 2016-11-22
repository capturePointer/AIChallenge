from scipy.stats import kurtosis, skew, entropy
from sklearn import svm, tree
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
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
		names = x_vars[0]
		x_vars = x_vars[1:]
		x_vars = np.array(x_vars)
		y_vars = np.array(y_vars)
		variables['x_vars'] = x_vars
		variables['y_vars'] = y_vars
		variables['names'] = names
		return variables

def train_dtc(variables):
	clf = tree.DecisionTreeClassifier()
	clf.fit(variables['x_vars'], variables['y_vars'])
	return clf

def train_svm(variables):
	svc = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, \
		cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=None, random_state=None)
	svc.fit(variables['x_vars'], variables['y_vars'])
	return svc

def train_rfc(variables):
	rfc = RandomForestClassifier()
	rfc.fit(variables['x_vars'], variables['y_vars'])
	return rfc

def get_feature_importances(rfc, variables):
	print "Features sorted by their score:"
	print sorted(zip(map(lambda x: round(x, 4), rfc.feature_importances_), variables['names']), 
	             reverse=True)

if __name__ == "__main__":
	variables = read_data('voice.csv')
	clf = train_dtc(variables)
	with open('voice_recognition.pkl', 'wb') as fid:
		cPickle.dump(clf, fid)
	svm = train_svm(variables)
	with open('voice_recognition_svm.pkl', 'wb') as fid:
		cPickle.dump(svm, fid)
	rfc = train_rfc(variables)
	with open('voice_recognition_rfc.pkl', 'wb') as fid:
		cPickle.dump(rfc, fid)
	get_feature_importances(rfc, variables)