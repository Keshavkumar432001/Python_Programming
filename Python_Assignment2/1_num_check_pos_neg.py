## Q1 Write a program to check whether a given number is positive, negative, or zero.

num = float(input("Enter The Number: "))

#Check whether given number is equal to zero.
if(num == 0):
    print("Entered Number Is Equal To Zero")

#If Number is not equals to zero,Check whether number is greater then zero.
elif(num > 0):
    print("Entered Number Is Positive")
#Number is neither equals to zero nor greater then zero.    
else:
    print("Entered Number Is Negative")