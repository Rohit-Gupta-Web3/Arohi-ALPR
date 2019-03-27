#!/bin/usr/env python3
from tkinter import *
import tkinter.filedialog as filedialog, os, subprocess as sub, sqlite3, locale, shutil,time, tkinter.messagebox
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'C')
count=0

def folder_move(buss,dev):
		global count
		c=sqlite3.connect("Aarohi.db")
		cu = c.cursor()
		cu.execute("SELECT ccode FROM Bussiness WHERE bid=?", (buss,)) 
		c_code=str(cu.fetchall()[0][0]).rstrip('\n')
		cu.execute("SELECT infol FROM Bussiness WHERE bid=?", (buss,)) 
		input_folder=str(cu.fetchall()[0][0]).rstrip('\n')+"/"+dev+"/"
		cu.execute("SELECT pfol FROM Bussiness WHERE bid=?", (buss,)) 
		processed_folder=str(cu.fetchall()[0][0]).rstrip('\n')+"/"
		cu.execute("SELECT unfol FROM Bussiness WHERE bid=?", (buss,)) 
		unprocessed_folder=str(cu.fetchall()[0][0]).rstrip('\n')+"/"
		cu.execute("SELECT Dip FROM Device WHERE Did=?", (dev,)) 
		cip=str(cu.fetchall()[0][0]).rstrip('\n')
		pwd = os.path.dirname(os.path.realpath(__file__)).rstrip('\n')
		onlyfiles = [ f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) ]
		if len(onlyfiles)==0:
			time.sleep(10)
			response = os.system("ping -c 1 " + cip)
			count=count+1
			if count >2:
				print("No files to process")
				time.sleep(1)
				tkinter.messagebox.showerror('Camera is not replying!')
				count=0
		i = 0
		while i < len(onlyfiles):
			os.chdir(input_folder)
			intime=time.ctime(os.path.getctime(onlyfiles[i]))
			p1 = sub.Popen(['alpr', '-c',c_code,'--clock', onlyfiles[i]], stdout=sub.PIPE)
			output = p1.communicate()[0]
			old_nm=input_folder+str(onlyfiles[i])
			output=str(output.decode('utf-8'))
			output=output.split()
			a=0
			while a< len(output):
				if output[a] == "license":
					print("file not processed")
					c.execute("insert into unprocessed values (?,?,?,?,?) ", (buss, dev, onlyfiles[i], intime, str(output)))
					c.commit()
					shutil.move(old_nm,unprocessed_folder)
				elif output[a] == "results":
					print(buss, dev, output[15], output[17])
					c.execute("insert into alpr values (?,?,?,?,?,?) ", (buss, dev, intime, str(output[5]), str(output[15]), str(output[17])))
					c.commit()
					new_nm=processed_folder+(str(output[15])+".jpg")
					shutil.move(old_nm,new_nm)
				a=a+1
			os.chdir(pwd)
			i += 1

if __name__=="__main__":
	#buss="rohit"
	c=sqlite3.connect("Aarohi.db")
	cu = c.cursor()
	cu.execute("SELECT * FROM Bussiness ORDER BY bid ASC LIMIT 1")
	buss=str(cu.fetchall()[0][0]).rstrip('\n')
	cu.execute("SELECT bid FROM Bussiness WHERE bid=?", (buss,)) 
	bid=str(cu.fetchall()[0][0]).rstrip('\n')
	cu.execute("SELECT Did FROM device WHERE bid=?", (buss,)) 
	d=cu.fetchall()
	c.execute('''CREATE TABLE if not exists alpr
			(Bid text(15), Did text(15), In_time blob, processing_time blob, Plate_no text(20), Confidence float(4))''')
	c.execute('''CREATE TABLE if not exists unprocessed
			(Bid text(15), Did text(15), file_name blob, In_time blob, reason text(100))''')
	c.commit()
	while(1):
		for k in d:
			for a in k:
				did=str(a)
				folder_move(bid,did)
