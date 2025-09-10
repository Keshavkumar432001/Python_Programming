## Q2 Write a program to check whether a given integer is even or odd.
num = int(input("Enter an integer: "))

# Check num divisible by 2 or not
if num % 2 == 0:
    print(f"{num} is Even Number.")
# If the above condition is false, then the number must be odd
else:
    print(f"{num} is Odd Number.")