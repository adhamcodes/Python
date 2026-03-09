"""Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on"""

num = int(input("Enter a number from 1 to 12: "))

if num == 1:
    print("January, 31 days")
elif num == 2:
    print("February, 28 days")
elif num == 3:
    print("March, 31 days")
elif num == 4:
    print("April, 30 days")
elif num == 5:
    print("May, 31 days")
elif num == 6:
    print("June, 30 days")
elif num == 7:
    print("July, 31 days")
elif num == 8:
    print("August, 31 days")
elif num == 9:
    print("September, 30 days")
elif num == 10:
    print("October, 31 days")
elif num == 11:
    print("November, 30 days")
elif num == 12:
    print("December, 31 days")
else:
    print("Invalid input. Please enter a number from 1 to 12.")