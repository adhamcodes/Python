"""Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Taj Mahal
                  Jaipur                              Jal Mahal"""


city = input("Enter the name of the city: ")
if city.lower() == "delhi":
    print("The monument of Delhi is Red Fort.")
elif city.lower() == "agra":
    print("The monument of Agra is Taj Mahal.")
elif city.lower() == "jaipur":
    print("The monument of Jaipur is Jal Mahal.")
else:
    print("Monument not found for the entered city.")