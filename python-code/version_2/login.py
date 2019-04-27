#!/bin/usr/env python3
from tkinter import *
import tkinter.filedialog as filedialog, tkinter.messagebox, os, subprocess as sub, sqlite3

master = Tk()
master.title('Launch Window')
master.geometry('350x300')
user = 'aarohi'
pas = 'aarohi'

def login():
	global master
	if not os.path.isfile('login.txt'):
		sub.call(['touch', 'login.txt'])
	f = open('login.txt', 'w')
	f.write(user)
	f.write(pas)
	f = open('login.txt', 'r')
	logi = f.read().rstrip('\n')
	vlogi = uid.get() + pswd.get()
	if str(logi) == str(vlogi):
		Button(master, text='Bussiness Setup', command=buss_fn).grid(row=5, column=0, sticky=N, pady=4)
		Button(master, text='Device Setup', command=dev_fn).grid(row=5, column=1, sticky=N, pady=4)
		Button(master, text='Continuing with APLR', command=alpr).grid(row=6, column=0, sticky=N, pady=4)
		master.update()
	else:
		tkinter.messagebox.showerror('Please check the username and password!')
	f.close()

def exit():
	result = tkinter.messagebox.askquestion('Quit', 'Are You Sure?', icon='warning')
	if result == 'yes':
		master.quit()

def buss_fn():
	sub.call(['python3', 'bussiness.cpython-36.pyc'])

def dev_fn():
	sub.call(['python3', 'device.cpython-36.pyc'])
	result = tkinter.messagebox.askquestion('Device Setup', 'Do you want to enter more?', icon='info')
	if result == 'yes':
		sub.call(['python3', 'device.cpython-36.pyc'])

def alpr():
	con=sqlite3.connect("Aarohi.db")
	cursor = con.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Bussiness';")
	if len(cursor.fetchall())==0:
		tkinter.messagebox.showinfo('Please Create ateast one bussiness id ')
		sub.call(['python3', 'bussiness.cpython-36.pyc'])	
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Device';")
		if len(cursor.fetchall())==0:
			tkinter.messagebox.showinfo('Please Create ateast one device id ')
			sub.call(['python3', 'device.cpython-36.pyc'])
	else:
		sub.call(['python3', 'launch.cpython-36.pyc'])

def main():
	global uid,pswd,lid
	Label(master, text=' Username *').grid(row=0, sticky=N, pady=4)
	Label(master, text=' Password *').grid(row=1, sticky=N, pady=4)
	Label(master, text=' License ID *').grid(row=2, sticky=N, pady=4)

	uid = Entry(master)
	pswd = Entry(master,show="*")
	lid = Entry(master)
	uid.grid(row=0, column=1, sticky=N, pady=4)
	pswd.grid(row=1, column=1, sticky=N, pady=4)
	lid.grid(row=2, column=1, sticky=N, pady=4)

	Button(master, text='login', command=login).grid(row=4, column=0, sticky=N, pady=4)
	Button(master, text='Exit', command=exit).grid(row=4, column=1, sticky=N, pady=4)

if __name__=="__main__":
	main()
	mainloop()
