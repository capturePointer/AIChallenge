#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from prediction import get_model, get_file_attributes, classify, play_sample, record_and_classify
import ttk

class App(Frame):
	def __init__(self, parent):
		mainframe = ttk.Frame(root, padding="12 12 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)
		filename = StringVar()
		dtc = StringVar()
		svm = StringVar()
		rfc = StringVar()
		ttk.Button(mainframe, text="Play sample Nº 1", command=lambda:play_sample('lana.wav')).grid(column=0, row=0, sticky=W)
		ttk.Button(mainframe, text="Play sample Nº 2", command=lambda:play_sample('corey.wav')).grid(column=0, row=1, sticky=W)
		ttk.Button(mainframe, text="Play sample Nº 3", command=lambda:play_sample('mia.wav')).grid(column=0, row=2, sticky=W)
		ttk.Button(mainframe, text="Play sample Nº 4", command=lambda:play_sample('emily.wav')).grid(column=0, row=3, sticky=W)
		ttk.Button(mainframe, text="Play sample Nº 5", command=lambda:play_sample('stephen.wav')).grid(column=0, row=4, sticky=W)
		ttk.Radiobutton(mainframe, text="Sample Nº 1", variable=filename, value='lana.wav').grid(column=3, row=0, sticky=E)
		ttk.Radiobutton(mainframe, text="Sample Nº 2", variable=filename, value='corey.wav').grid(column=3, row=1, sticky=E)
		ttk.Radiobutton(mainframe, text="Sample Nº 3", variable=filename, value='mia.wav').grid(column=3, row=2, sticky=E)
		ttk.Radiobutton(mainframe, text="Sample Nº 4", variable=filename, value='emily.wav').grid(column=3, row=3, sticky=E)
		ttk.Radiobutton(mainframe, text="Sample Nº 5", variable=filename, value='stephen.wav').grid(column=3, row=4, sticky=E)
		ttk.Button(mainframe, text="Classify from sample", command=lambda:classify(dtc, svm, rfc, filename, mainframe, False)).grid(column=3, row=5, sticky=W)
		ttk.Button(mainframe, text="Classify form microphone", command=lambda:record_and_classify(dtc, svm, rfc, mainframe, True)).grid(column=3, row=6, sticky=W)
		ttk.Label(mainframe, text= "Decision Tree: ").grid(column=2, row=7, sticky=E)
		ttk.Label(mainframe, text= "Support Vector Machine: ").grid(column=2, row=8, sticky=E)
		ttk.Label(mainframe, text= "Random Forest: ").grid(column=2, row=9, sticky=E)
		ttk.Label(mainframe, textvariable=dtc).grid(column=3, row=7, sticky=E)
		ttk.Label(mainframe, textvariable=svm).grid(column=3, row=8, sticky=E)
		ttk.Label(mainframe, textvariable=rfc).grid(column=3, row=9, sticky=E)

if __name__ == "__main__":
	root = Tk()
	root.title("Voice gender classifier")
	App(root)
	root.mainloop()