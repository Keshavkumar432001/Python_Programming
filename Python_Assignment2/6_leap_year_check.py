## Q6 Write a program to check whether a given year is a leap year or not. (Hint: A leap year is divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter a year: "))

if year % 400 == 0:
    # If divisible by 400 means it's Leap year
    print(f"{year} is a Leap Year.")
elif year % 100 == 0:
    # If divisible by 100 but not by 400 then it means not a leap year
    print(f"{year} is not a Leap Year.")
elif year % 4 == 0:
    # If divisible by 4 but not by 100 means it's Leap year
    print(f"{year} is a Leap Year.")
else:
    # All other years the not a leap year
    print(f"{year} is not a Leap Year.")