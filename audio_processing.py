from numpy import *
import scipy as sp
from pandas import *
import pandas.rpy.common as com
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import os
modulePath =  os.getcwd() + '/src/'
print(modulePath)
import sys
sys.path.append(modulePath)
import dspUtil
from scipy.stats import kurtosis, skew, entropy
from sklearn import svm
import pyaudio
import wave
import numpy as np
import csv
#from voice_gender_recognition import read_track

audio = importr('warbleR')

def read_track(track_name):
	frequencies = []
	chunk = 2048
	# open up a wave
	wf = wave.open(track_name, 'rb')
	swidth = wf.getsampwidth()
	RATE = wf.getframerate()
	# use a Blackman window
	window = np.blackman(chunk)
	# open stream
	p = pyaudio.PyAudio()
	stream = p.open(format =
	                p.get_format_from_width(wf.getsampwidth()),
	                channels = wf.getnchannels(),
	                rate = RATE,
	                output = True)
	# read some data
	data = wf.readframes(chunk)
	# play stream and find the frequency of each chunk
	while len(data) == chunk*swidth:
	   # write data out to the audio stream
	   stream.write(data)
	   # unpack the data and times by the hamming window
	   indata = np.array(wave.struct.unpack("%dh"%(len(data)/swidth),\
	                                         data))*window
	   # Take the fft and square each value
	   fftData=abs(np.fft.rfft(indata))**2
	   # find the maximum
	   which = fftData[1:].argmax() + 1
	   # use quadratic interpolation around the max
	   if which != len(fftData)-1:
	      y0,y1,y2 = np.log(fftData[which-1:which+2:])
	      x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
	        # find the frequency and output it
	      thefreq = (which+x1)*RATE/chunk
	      #print "The freq is %f Hz." % (thefreq)
	      khz = thefreq/1000
	      frequencies.append(khz)
	      segs = 0.05*60
	      #print(khz/segs)
	   else:
	      thefreq = which*RATE/chunk
	      #print "The freq is %f Hz." % (thefreq)
	      #print(thefreq/.05)
	    # read some more data
	   data = wf.readframes(chunk)
	if data:
	   stream.write(data)
	stream.close()
	p.terminate()
	frequencies = np.array(frequencies)
	input_data = []
	input_data.append(np.mean(frequencies))
	input_data.append(np.std(frequencies))
	input_data.append(np.median(frequencies))
	input_data.append(np.percentile(frequencies, 25))
	input_data.append(np.percentile(frequencies, 75))
	input_data.append(np.percentile(frequencies, 50))
	input_data.append(skew(frequencies))
	input_data.append(kurtosis(frequencies))
	input_data.append(dspUtil.calculateSpectralFlatness(frequencies))
	input_data.append(dspUtil.calculateSpectralFlatness(frequencies))
	return input_data
d = {'start': ro.r(0), 'end': ro.r(5), "sound.files": "100hz.wav", "selec": ro.r(0)}
inp = ro.DataFrame(d)
x = audio.specan(inp)
print(x)
#data = read_track("100hz.wav")