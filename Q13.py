"""Write a program to find the lowest number out of two numbers excepted from user."""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 < num2:
    print(f"The lowest number is: {num1}")
elif num2 < num1:
    print(f"The lowest number is: {num2}")
else:
    print("Both numbers are equal.")