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
	      print "The freq is %f Hz." % (thefreq)
	      khz = thefreq/1000
	      frequencies.append(khz)
	      segs = 0.05*60
	      #print(khz/segs)
	   else:
	      thefreq = which*RATE/chunk
	      print "The freq is %f Hz." % (thefreq)
	      print(thefreq/.05)
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

def calculate_input():
	pass

print(read_track("100hz.wav"))

x_vars = []
y_vars = []

def read_data():
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

x_vars = x_vars[1:]

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(x_vars, y_vars)

"""
meanfreq: mean frequency (in kHz)
sd: standard deviation of frequency
median: median frequency (in kHz)
Q25: first quantile (in kHz)
Q75: third quantile (in kHz)
IQR: interquantile range (in kHz)
skew: skewness (see note in specprop description)
kurt: kurtosis (see note in specprop description)

sp.ent: spectral entropy

sfm: spectral flatness

mode: mode frequency
centroid: frequency centroid (see specprop)
peakf: peak frequency (frequency with highest energy)
meanfun: average of fundamental frequency measured across acoustic signal
minfun: minimum fundamental frequency measured across acoustic signal
maxfun: maximum fundamental frequency measured across acoustic signal
meandom: average of dominant frequency measured across acoustic signal
mindom: minimum of dominant frequency measured across acoustic signal
maxdom: maximum of dominant frequency measured across acoustic signal
dfrange: range of dominant frequency measured across acoustic signal
modindx: modulation index. Calculated as the accumulated absolute difference between adjacent measurements of fundamental frequencies divided by the frequency range
label: male or female
"""

print(clf.predict([[0.0597809849598081,0.0642412677031359,0.032026913372582,0.0150714886459209,0.0901934398654331,0.0751219512195122,12.8634618371626,274.402905502067,0.893369416700807,0.491917766397811,0,0.0597809849598081,0.084279106440321,0.0157016683022571,0.275862068965517,0.0078125,0.0078125,0.0078125,0,0]]))







