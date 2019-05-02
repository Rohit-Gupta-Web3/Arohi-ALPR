#!/bin/usr/env python3
from tkinter import *
import tkinter.filedialog as filedialog, os, subprocess as sub, sqlite3, locale, shutil,time, tkinter.messagebox, string, random
locale.setlocale(locale.LC_ALL, 'C')
count=0

def folder_move(buss,dev):
		global count
		c=sqlite3.connect("Aarohi.db")
		cu = c.cursor()
		cu.execute("SELECT ccode FROM Bussiness WHERE bid=?", (buss,)) 
		c_code=str(cu.fetchall()[0][0]).rstrip('\n')
		cu.execute("SELECT infol FROM Device WHERE did=?", (dev,)) 
		input_folder=str(cu.fetchall()[0][0]).rstrip('\n')+"/"
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
			if count == 2:
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
					only=input_folder+onlyfiles[i]
					p1 = sub.Popen(['python3','/home/rohit/Arohi-ALPR/python-code/version_2/__pycache__/plate_recognition.cpython-36.pyc', only], stdout=sub.PIPE)
					result = p1.communicate()[0]
					result=result.decode('utf-8')
					result=result.split()
					b=0
					while b< len(result):
						if result[b] == "\"error\":":
							print("file not processed")
							print("PlateRecognizer");
							for j in result:
								result=' '.join(str(result[j]))
							c.execute("insert into unprocessed values (?,?,?,?,?) ", (buss, dev, onlyfiles[i], intime, str(result)))		
							c.commit()
							shutil.move(old_nm,unprocessed_folder+str(id_generator())+".jpg")
						elif result[b] == "\"results\":":
							print("PlateRecognizer");
							c.execute("insert into alpr values (?,?,?,?,?,?) ", (buss, dev, intime , str(result[3]), str(result[21]), str(result[23])))
							c.commit()
							result[21]=str(result[21]).strip(",")
							result[21]=str(result[21]).strip('\"')
							result[21]=str(result[21]).swapcase()
							print(buss, dev, result[3], result[21], result[23])
							new_nm=processed_folder+(str(result[21])+"_"+str(id_generator())+".jpg")
							shutil.move(old_nm,new_nm)
						b=b+1
				elif output[a] == "results":
					print(buss, dev, output[5], output[15], output[17])
					c.execute("insert into alpr values (?,?,?,?,?,?) ", (buss, dev, intime, str(output[5]), str(output[15]), str(output[17])))
					c.commit()
					new_nm=processed_folder+(str(output[15])+"_"+str(id_generator())+".jpg")
					shutil.move(old_nm,new_nm)
				a=a+1
			os.chdir(pwd)
			i += 1

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

if __name__=="__main__":
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
