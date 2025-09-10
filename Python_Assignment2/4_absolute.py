## Q4 Write a program to find the absolute value of a given number without using the abs() function.

num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    # If the number is negative then multiply by -1 to make it positive
    absolute_value = -num
else:
    # If the number is already positive or zero just do nothing
    absolute_value = num

print(f"The absolute value of {num} is {absolute_value}")