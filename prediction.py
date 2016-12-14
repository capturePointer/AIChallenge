from scipy.stats import kurtosis, skew, entropy
from rpy2.robjects.packages import importr
from numpy import *
from pandas import *
from sklearn import svm
from pygame import mixer
from pygame.mixer import music
import scipy as sp
import pandas.rpy.common as com
import rpy2.robjects as ro
import numpy as np
import cPickle
import pyaudio
import wave
import sys
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
	for (i, data) in enumerate(data_list):
		if i is not 12:
			raw_data.append(data[0])
	return raw_data

def get_model(model_name):
	with open(model_name, 'rb') as fid:
		clf = cPickle.load(fid)
	return clf

def play_sample(filename):
	mixer.init()
	music.load(filename)
	music.play(0)

def classify(dtc, svm, rfc, filename, mainframe, local):
	classify_dtc(dtc, filename, mainframe, local)
	classify_svm(svm, filename, mainframe, local)
	classify_rfc(rfc, filename, mainframe, local)

def classify_dtc(label_text, filename, mainframe, local):
	clf = get_model('voice_recognition.pkl')
	if local is False:
		attributes = get_file_attributes(filename.get())
	else:
		attributes = get_file_attributes(filename)
	x = clf.predict([attributes])
	if x == [0]:
		x = "Male"
	elif x == [1]:
		x = "Female"
	label_text.set(x)
	mainframe.update_idletasks()

def classify_svm(label_text, filename, mainframe, local):
	svc = get_model('voice_recognition_svm.pkl')
	if local is False:
		attributes = get_file_attributes(filename.get())
	else:
		attributes = get_file_attributes(filename)
	x = svc.predict([attributes])
	if x == [0]:
		x = "Male"
	elif x == [1]:
		x = "Female"
	label_text.set(x)
	mainframe.update_idletasks()

def classify_rfc(label_text, filename, mainframe, local):
	rfc = get_model('voice_recognition_rfc.pkl')
	if local is False:
		attributes = get_file_attributes(filename.get())
	else:
		attributes = get_file_attributes(filename)
	x = rfc.predict([attributes])
	if x == [0]:
		x = "Male"
	elif x == [1]:
		x = "Female"
	label_text.set(x)
	mainframe.update_idletasks()

def record_and_classify(dtc, svm, rfc, mainframe, local):
	# Code taken from https://gist.github.com/mabdrabo/8678538
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "file.wav" 
	audio = pyaudio.PyAudio()
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print "recording..."
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	print "finished recording"
	stream.stop_stream()
	stream.close()
	audio.terminate()
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	classify(dtc, svm, rfc, 'file.wav', mainframe, local)