#program  about who can drive:
#Enter the age:
age=(int(input("Enter the age of the person:")))
if age>18:
	print("Yes,you can drive!!!")

elif age==18:
	print("Can't decide, give a physical test.")

else:
	print("Sorry, you Can't drive.")
  
 #program about swapping two numbers:
 #we first enter two numbers.
 #Then swap them
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("Original numbers:",n1,n2)
n1,n2=n2,n1
print("After swapping:",n1,n2)
