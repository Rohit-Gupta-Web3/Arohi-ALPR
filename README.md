# Arohi-ALPR
This is a application build using OpenALPR and Python

### Dependencies:
1. OpenALPR
2. Python3.6
3. Tkinter
4. SQLite3

### Install all the dependencies
```
sudo chmod 777 run.sh
./run.sh
```

### To execute
```
1. Through GUI:   click on the desktop icon, Aarohi.desktop
'''
'''
2. Through CLI:	  execute the following commands:
	2.1 grep '^Exec' Aarohi.desktop | tail -1 | sed 's/^Exec=//' | sed 's/%.//' | sed 's/^"//g' | sed 's/" *$//g'` &
	2.2 python3 logic.cpython-36.pyc
```

### The Output can be found out by the following commands:
```
sqlitebrowser Aarohi.db
```

### Images Folder
Some Images for testing has been provided in the Folder

### Tips
1. kindly move the traineddata file for your country out of the tessdata

### India 
OpenALPR requisite files for India
