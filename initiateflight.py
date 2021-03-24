"""
This module is used for allocation of business rows and economy rows in the flight.
Run this module only once.
"""

import pickle
from flight import Seats

def initiateflight():
    # initialising the number of rows in business class and economy class
    brows = input("Enter rows in Business class: ")
    erows = input("Enter rows in Economy class: ")
    return brows, erows

if __name__ == "__main__":
    brows, erows = initiateflight()
    category = dict()
    category['business_rows'] = int(brows)
    category['economy_rows'] = int(erows)

    with open("flight_seat.pkl",'wb') as flight:
        pickle.dump(category,flight)


    #Depending upon business rows and economy rows provided, seat matrix will be formed
    Flight = Seats(brows, erows)
    genre = dict()
    seattype = Flight.category()
    genre['window'] = seattype[0]
    genre['middle'] = seattype[1]
    genre['aisle'] = seattype[2]

    with open('available_seat.pkl','wb') as available:
        pickle.dump(genre, available)

    # Creating a new list of passengers when new flight is allocated
    passengers = dict()
    with open("passengers_data.pkl", 'wb') as passenger_data:
        pickle.dump(passengers, passenger_data)

    print("Successfully seats are allocated in the flight")
    close = input('Press q to exit: ')