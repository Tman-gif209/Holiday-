#For this task i am required to calculate a user's holiday cost including the plane cost, hotel cost and car rental cost.

# I will need to create a function for hotel_cost.
def hotelcost(num_night):
    hotel_cost = num_night * 1100
    print(f"The hotel cost is {hotel_cost}.")
    return hotel_cost

#Now I will need a function for plane cost.
def planecost(city_flights):
    if city_flights == "D":
        plane_cost = 4500
        print(f"The plane price is {plane_cost}.")
        return plane_cost
    
    elif city_flights == "B":
        plane_cost = 2430
        print(f"The plane price is {plane_cost}")
        return plane_cost
    
    elif city_flights == "CT":
        plane_cost = 2000
        print(f"The plane price is {plane_cost}")
        return plane_cost
    
    else: 
        print("Incorrect entry.")

#Now I will create a function to calculate the total cost of the car rental.
def rentalcost(rental_days):
    rental_cost = rental_days * 500
    print(f"Your total rental cost is {rental_cost}.")
    return rental_cost

#Now I will do a create the last function to add the prices of the 3 functions above to get a total cost.(holiday cost)
def holidaycost(num1, num2, num3):
    holiday_cost = num1 + num2 + num3
    print(f" \nYour holiday cost is R{holiday_cost}.")
    return holiday_cost

print('''Here is a list of cities and the prices:
 D = Dubai - 4500
 B = Bangkok - 2430
 CT = Cape Town - 2000

Enter the initials of the city that you choose below.''')
city_flights = input(" ")
city_flight = planecost(city_flights)

print(" \n Enter the number of days that you will be hiring a car for below.")
rental_days = int(input(" "))
rental = rentalcost(rental_days)

print("\n Enter the number of nights that you intend to be there below.")
num_night = int(input(" "))
num_nights = hotelcost(num_night)

#The calculation used to get the total.
total = holidaycost(city_flight, rental, num_nights)



