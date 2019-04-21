#!bin/usr/env python3
from tkinter import *
import tkinter.filedialog as filedialog, tkinter.messagebox,subprocess as sub, sqlite3, socket

master = Tk()
master.title('Bussiness Setup')
master.geometry('500x300')

input_path = StringVar()
processed_path = StringVar()
unprocessed_path = StringVar()
tkvar = StringVar()
OPTIONS = [
 'Choose Your Country',
 'Australia',
 'Argentina',
 'Brazil',
 'China',
 'Canada',
 'Europe',
 'Great Britain',
 'Indonesia',
 'India',
 'Japan',
 'Mexico',
 'New Zealand',
 'South Africa',
 'South Arabia',
 'South Korea',
 'UAE',
 'USA',
 'Thailand']

def input_folder():
	global inp,input_path
	inp = filedialog.askdirectory()
	input_path.set(inp)

def processed_folder():
	global pro,processed_path
	pro = filedialog.askdirectory()
	processed_path.set(pro)

def unprocessed_folder():
	global unpro,unprocessed_path
	unpro = filedialog.askdirectory()
	unprocessed_path.set(unpro)

def insert_entry_fields():
	buss = bid.get()
	tkvar.trace('w', country_code())
	if len(buss) == 0:
		tkinter.messagebox.showwarning('Warning', 'Bussiness ID not Eneterd')
	elif c_code == OPTIONS[0]:
		tkinter.messagebox.showwarning('Warning', 'Country Code not Eneterd')
	elif len(inp) == 0:
		tkinter.messagebox.showwarning('Warning', 'Input Folder Path not selected')
	elif len(pro) == 0:
		tkinter.messagebox.showwarning('Warning', 'Processed Folder Path not selected')
	elif len(unpro) == 0:
		tkinter.messagebox.showwarning('Warning', 'Unprocessed Folder Path not selected')
	else:
		c=sqlite3.connect("Aarohi.db")
		c.execute('''CREATE TABLE if not exists Bussiness
			(Bid text(15), ccode text(2), infol blob, pfol blob, unfol blob, primary key(Bid))''')
		c.execute("insert into Bussiness values (?, ?, ?, ?, ?)",( buss, c_code, inp, pro, unpro))
		c.commit()
		c.close()
	window_quit(0)

def country_code():
	global c_code
	if tkvar.get() == 'USA':
		c_code = 'us'
	elif tkvar.get() == 'Europe':
		c_code = 'eu'
	elif tkvar.get() == 'Thailand':
		c_code = 'thi'
	elif tkvar.get() == 'India':
		c_code = 'in'
	elif tkvar.get() == 'China':
		c_code = 'cn'
	elif tkvar.get() == 'Australia':
		c_code = 'au'
	elif tkvar.get() == 'Brazil':
		c_code = 'br'
	elif tkvar.get() == 'South Korea':
		c_code = 'kr'
	elif tkvar.get() == 'Mexico':
		c_code = 'mx'

def window_quit(x=1):
	global master
	if x == 0:
		result = tkinter.messagebox.askquestion('Submit', 'Are You Sure?', icon='warning')
	else:
		result = tkinter.messagebox.askquestion('Quit', 'Are You Sure?', icon='warning')
	if result == 'yes':
		master.quit()

def clear():
	bid.delete(0, END)
	input_path.set('')
	processed_path.set('')
	unprocessed_path.set('')
	tkvar.set(OPTIONS[0])

def main_l():
	global bid
	Label(master, text=' Bussiness ID *').grid(row=0, sticky=N, pady=4)
	Label(master, text=' Country *').grid(row=1, sticky=N, pady=4)
	Label(master, text=' Input Folder *').grid(row=2, sticky=N, pady=4)
	Label(master, text=' Processed Files *').grid(row=3, sticky=N, pady=4)
	Label(master, text=' Unprocessed Files *').grid(row=4, sticky=N, pady=4)

	infol = Label(master, textvariable=input_path).grid(row=2, column=2, sticky=N, pady=4)
	profol = Label(master, textvariable=processed_path).grid(row=3, column=2, sticky=N, pady=4)
	unprofol = Label(master, textvariable=unprocessed_path).grid(row=4, column=2, sticky=N, pady=4)

	bid = Entry(master)
	bid.grid(row=0, column=1, sticky=N, pady=4)
	bid.insert(0, '')
	inp = ''
	pro = ''
	unpro = ''
	tkvar.set(OPTIONS[0])

	Button(master, text='Browse', command=input_folder).grid(row=2, column=1, sticky=N, pady=4)
	Button(master, text='Browse', command=processed_folder).grid(row=3, column=1, sticky=N, pady=4)
	Button(master, text='Browse', command=unprocessed_folder).grid(row=4, column=1, sticky=N, pady=4)
	Button(master, text='Quit', command=window_quit).grid(row=5, column=0, sticky=N, pady=4)
	Button(master, text='Submit', command=insert_entry_fields).grid(row=5, column=1, sticky=N, pady=4)
	Button(master, text='Clear', command=clear).grid(row=5, column=2, sticky=N, pady=4)

	mainframe = Frame(master)
	mainframe.grid(column=1, row=1, sticky=N)
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)
	popupMenu = OptionMenu(mainframe, tkvar, *OPTIONS)
	popupMenu.grid(row=2, column=2)

	mainframe = Frame(master)
	mainframe.grid(column=1, row=1, sticky=N)
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

if __name__=="__main__":
	main_l()
	mainloop()
