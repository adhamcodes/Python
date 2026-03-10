"""Write a program to check whether a number entered is three digit number or not."""
number = int(input("Enter a number: "))
if 100 <= number <= 999:
    print(f"{number} is a three-digit number.")
else:
    print(f"{number} is not a three-digit number.")