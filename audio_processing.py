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

audio = importr('warbleR')

def get_file_attributes(filename):
	d = {'start': ro.r(0), 'end': ro.r(5), "sound.files": filename, "selec": ro.r(0)}
	inp = ro.DataFrame(d)
	x = audio.specan(inp, bp = ro.IntVector((0,22)), wl = 2048, threshold = 5, parallel = 1)
	data_list = x[3:]
	raw_data = []
	print(x)
	for data in data_list:
		raw_data.append(data[0])
	return raw_data
	#print(raw_data)
