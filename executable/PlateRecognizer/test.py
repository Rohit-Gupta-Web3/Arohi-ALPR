#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
from tkinter import *
import tkinter.filedialog as filedialog, tkinter.messagebox,subprocess as sub, os

master = Tk()
master.title('ALPR Test')

def path():
	input_folder = filedialog.askdirectory()
	input_folder= input_folder+"/"
	print(input_folder)
	onlyfiles = [ f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) ]
	if len(onlyfiles)==0:
		print("no Files")
	i = 0
	while i < len(onlyfiles):
		only=input_folder+onlyfiles[i]
		p1 = sub.Popen(['python3','plate_recognition.py', only], stdout=sub.PIPE)
		result = p1.communicate()[0]
		result=str(result.decode('utf-8'))
		print(result)
		print("\n")
		i=i+1
	master.quit()

def main():
	Button(master, text='Path', command=path).grid(row=0, column=1, sticky=N, pady=4, padx=4)
	Button(master, text='Exit', command=master.quit).grid(row=0, column=2, sticky=N, pady=4, padx=4)

if __name__=="__main__":
	main()
	mainloop()
