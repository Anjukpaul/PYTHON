stud={} 
n=int(input("Enter the number of students:"))
for i in range(0,n):
	a=input("Enter the name of student:")
	stud[a]=int(input("Enter the mark of student:"))
print(stud)
b=[]
b+=stud.keys()# append each key value pair to a list named b
b.sort()
for i in range(n):
	print("%s\t\t\t%d" %(b[i],stud[b[i]]))	
