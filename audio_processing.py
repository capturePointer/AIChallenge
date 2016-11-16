from numpy import *
import scipy as sp
from pandas import *
import pandas.rpy.common as com
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import sys
from scipy.stats import kurtosis, skew, entropy
from sklearn import svm
import pyaudio
import wave
import numpy as np
import csv
import os

r_source = ro.r['source']
r_source(os.getcwd() + '/sound.R')
specan3 = ro.globalenv['specan3']
warbler = importr('warbleR')
tuner = importr('tuneR')
seewave = importr('seewave')

def get_file_attributes(filename):
	d = {'start': ro.r(0), 'end': ro.r(5), "sound.files": filename, "selec": ro.r(0)}
	inp = ro.DataFrame(d)
	x = specan3(inp, bp = ro.IntVector((0,22)), wl = 2048, threshold = 5, parallel = 1)
	data_list = x[3:]
	raw_data = []
	print(x)
	for (i, data) in enumerate(data_list):
		if i is not 12:
			raw_data.append(data[0])
	return raw_data