f=input("Enter the filename:")
try:
	f1=open(f,"r")
except IOError:
	print("no file named",f)
except:
	print(f,"is in the system")