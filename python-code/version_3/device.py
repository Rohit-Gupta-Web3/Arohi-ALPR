from tkinter import *
import tkinter.filedialog as filedialog, tkinter.messagebox,subprocess as sub, sqlite3, socket, os

root=Tk()
root.title('Device ID')
root.geometry('400x150')
	
def main_l():
	global bid, did, dip
	Label(root, text=' Bussiness ID *').grid(row=0,column=0, sticky=N, pady=4)
	Label(root, text=' Device ID *').grid(row=1,column=0, sticky=N, pady=4)
	Label(root, text=' Device IP *').grid(row=2,column=0, sticky=N, pady=4)
	
	bid = Entry(root)
	did = Entry(root)
	dip = Entry(root)
	
	bid.grid(row=0, column=1, sticky=N, pady=4)
	did.grid(row=1, column=1, sticky=N, pady=4)
	dip.grid(row=2, column=1, sticky=N, pady=4)
	
	dip.insert(0, socket.gethostbyname(socket.gethostname()))

	Button(root, text='Submit', command=devpro).grid(row=3, column=0, sticky=N, pady=4)
	Button(root, text='Cancel..', command=quit).grid(row=3, column=1, sticky=N, pady=4)
	Button(root, text='clear', command=clear).grid(row=3, column=2, sticky=N, pady=4)	
	
def devpro():
	buss=bid.get()
	dev=did.get()
	cip=dip.get()
	
	if len(buss) == 0:
		tkinter.messagebox.showwarning('Warning', 'Device ID not Eneterd')
	elif len(dev) == 0:
		tkinter.messagebox.showwarning('Warning', 'Device ID not Eneterd')
	elif len(cip) == 0:
		tkinter.messagebox.showwarning('Warning', 'Device IP not Eneterd')
	else:
		c=sqlite3.connect("Aarohi.db")
		cu = c.cursor()
		cu.execute("SELECT bid FROM Bussiness WHERE bid=?", (buss,)) 
		if len(cu.fetchall()) !=0:
			c.execute('''CREATE TABLE if not exists Device 
			(Bid text(15), Did text(15), Dip blob)''')
			c.execute("insert into Device values (?, ?, ?)",( buss,dev,cip))
			cu.execute("SELECT infol FROM Bussiness WHERE bid=?", (buss,)) 
			input_folder=str(cu.fetchall()[0][0]).rstrip('\n')+"/"
			path=input_folder+dev
			c.commit()
			c.close()
			try:
    				os.makedirs(path)
			except FileExistsError:
   				pass
			quit(0)
		else:
			tkinter.messagebox.showerror('Error', 'Bussiness ID doesnot Exists')		

def clear():
	bid.delete(0, END)
	did.delete(0, END)
	dip.delete(0, END)

def quit(x=1):
	global root
	if x == 0:
		result = tkinter.messagebox.askquestion('Submit', 'Are You Sure?', icon='warning')
	else:
		result = tkinter.messagebox.askquestion('Quit', 'Are You Sure?', icon='warning')
	if result == 'yes':
		root.quit()
		
if __name__=="__main__":
	main_l()
	mainloop()
