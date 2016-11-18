#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from pygame import mixer
from pygame.mixer import music
from prediction import get_model, get_file_attributes
import ttk

def play_sample(filename):
	print("Playing " + filename)
	mixer.init()
	music.load(filename)
	music.play(0)

def classify(label_text, filename, mainframe):
	clf = get_model('voice_recognition.pkl')
	attributes = get_file_attributes(filename.get())
	x = clf.predict([attributes])
	if x == [0]:
		x = "Male"
	else:
		x = "Female"
	label_text.set(x)
	mainframe.update_idletasks()
    
root = Tk()
root.title("Voice gender classifier")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
filename = StringVar()
gender = StringVar()
ttk.Button(mainframe, text="Play sample Nº 1", command=lambda:play_sample('lana.wav')).grid(column=0, row=0, sticky=W)
ttk.Button(mainframe, text="Play sample Nº 2", command=lambda:play_sample('corey.wav')).grid(column=0, row=1, sticky=W)
ttk.Button(mainframe, text="Play sample Nº 3", command=lambda:play_sample('stephen.wav')).grid(column=0, row=2, sticky=W)
ttk.Button(mainframe, text="Play sample Nº 4", command=lambda:play_sample('emily.wav')).grid(column=0, row=3, sticky=W)
ttk.Button(mainframe, text="Play sample Nº 5", command=lambda:play_sample('mia.wav')).grid(column=0, row=4, sticky=W)
ttk.Radiobutton(mainframe, text="Sample Nº 1", variable=filename, value='lana.wav').grid(column=3, row=0, sticky=E)
ttk.Radiobutton(mainframe, text="Sample Nº 2", variable=filename, value='corey.wav').grid(column=3, row=1, sticky=E)
ttk.Radiobutton(mainframe, text="Sample Nº 3", variable=filename, value='stephen.wav').grid(column=3, row=2, sticky=E)
ttk.Radiobutton(mainframe, text="Sample Nº 4", variable=filename, value='emily.wav').grid(column=3, row=3, sticky=E)
ttk.Radiobutton(mainframe, text="Sample Nº 5", variable=filename, value='mia.wav').grid(column=3, row=4, sticky=E)
ttk.Button(mainframe, text="Make sample classification", command=lambda:classify(gender, filename, mainframe)).grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text= "Gender: ").grid(column=2, row=6, sticky=E)
ttk.Label(mainframe, textvariable=gender).grid(column=3, row=6, sticky=E)

root.mainloop()
