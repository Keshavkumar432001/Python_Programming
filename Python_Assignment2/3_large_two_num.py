## Q3 Write a program to input two numbers and print which one is larger.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the two numbers using if-else statement
if num1 > num2:
    # If first number is greater than second number
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    # If second number is greater than first number
    print(f"{num2} is larger than {num1}")
else:
    # If both numbers are equal
    print("Both numbers are equal")