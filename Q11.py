"""Write a program to check whether a person is eligible for voting or not.(voting age >=18)"""
age = int(input("Enter the age of the person: "))
if age >= 18:
    print("The person is eligible for voting.")
else:
    print("The person is not eligible for voting.")