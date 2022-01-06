n=int(input("enter number of students:"))
studlist=[]
for i in range(0,n):
	stud={}
	stud['name']=input("Enter name  ")
	stud["branch"]=input("Enter branch:  ")
	stud["roll no"]=int(input("Enter roll no:\n"))
	studlist.append(stud)
print("name  branch  roll no")
print()
print()
for i in range(0,n):	
	print(studlist[i])
