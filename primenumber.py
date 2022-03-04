num=int(input("enter a number"))
#prime number are greater than 1
if(num>1):
      for i in range(2,num):
               if(num%i==0):
                     print("not prime\n")
                     print(i,"times",num//i,"is",num)
                     break
#if break is not used else below will also be executed
      else:
                       print("it is a prime number")