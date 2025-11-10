import os 
import shutil
from_dir=input("enter the dir of the folder to protect")
fname=input("enter folder name to create")
pasw=input("enter the password")

todir="C:/Users/Aadithya Vikram/Documents"
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
	for j in range(0,10):
		path=os.path.join(todir,str(j))
		try:
			os.mkdir(path)
		except:
			print("error1")
		for k in range(1,11):
			path2=os.path.join(path,str(k))
			try:
				os.mkdir(path2)
			except:
				print("error2")
	todir=todir+'/'+i
try:
	shutil.move(from_dir,todir)
except:
	print()

