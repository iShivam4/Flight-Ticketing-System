"""

"""

import pickle
from flight import *

def details():
    name = input("Enter Name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    source = input("Enter from: ")
    destination = input("Enter to: ")

    return name, age, email, source, destination


if __name__ == "__main__":
    try:
        with open('flight_seat.pkl','rb') as flight:
            category = pickle.load(flight)
            business_rows = int(category['business_rows'])
            economy_rows = int(category['economy_rows'])

    except FileNotFoundError:
        print("Seat is yet not allocated. Please run the initiateflight.py for seats allocation")


    passenger = details()
    category_ = input("Enter Class you want to travel(Business or Economy): ")
    show = SeatMatrix(business_rows,economy_rows)
    show.matrix(category_)



    while True:
        S1 = SeatBooking()
        seat = input("Select a seat from the above chart : ")
        if S1.bookseat(seat) == True:
            S1.vacantseat()
            print("Seat available. Booking your SEAT....")
            print("Welcome on board Dear {}. Your ticket information is as follows.\n".format(passenger[0]))
            break
        else:
            print("Seat is not available. Please select another seat")
            continue

    P1 = Passenger_info(name = passenger[0], age = passenger[1],
                        email= passenger[2],seat = seat,category = category_,
                        source = passenger[3],destination = passenger[4])

    book_id = P1.generate_id()
    P1.ticket(book_id=book_id)
    P1.storeData(book_id = book_id)