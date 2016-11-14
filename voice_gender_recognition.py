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
	freq_sum = 0
	for frequency in frequencies:
		freq_sum += frequency
		print(frequency)
	mean = freq_sum/len(frequencies)
	print("meanfreq")
	print(mean)
	frequencies = np.array(frequencies)
	print(np.mean(frequencies))

def calculate_input():
	pass

read_track("100hz.wav")

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

"""for row in x_vars:
	print(row)
print(y_vars)"""

x_vars = x_vars[1:]

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(x_vars, y_vars)

"""SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)"""

print(clf.predict([[0.0597809849598081,0.0642412677031359,0.032026913372582,0.0150714886459209,0.0901934398654331,0.0751219512195122,12.8634618371626,274.402905502067,0.893369416700807,0.491917766397811,0,0.0597809849598081,0.084279106440321,0.0157016683022571,0.275862068965517,0.0078125,0.0078125,0.0078125,0,0]]))