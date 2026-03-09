"""Q2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                        Tax
        > 100000                                                  15%
        > 50000 and <= 100000                                     10%
        <= 50000                                                  5%
"""

cost = input("Enter the cost price of the bike: ")

cost = float(cost)

if cost > 100000:
    cost = cost + (cost * 0.15)
elif cost > 50000 and cost <= 100000:
    cost = cost + (cost * 0.10)
else:
    cost = cost + (cost * 0.05)

print("Road tax to be paid: ", cost)