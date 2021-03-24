"""
This file contains all the classes that are required to book a ticket in a flight.
"""

import uuid
import pickle
from datetime import datetime

__all__ = ['Generate','Seats','SeatMatrix','SeatBooking','Passenger_info']


class Generate(object):
    """
    Generate() is used to create a unique booking_id for passenger travelling.
    """

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def generate_id(self):
        id_ = uuid.uuid4()
        genid = (self.source[:3] + self.destination[:3] + str(id_)[-8:]).upper()
        return genid

# G1 = Generate(source="Pune", destination= "Delhi")
# print(G1.generate_id())

###################################################################################################

class SeatMatrix(object):
    """
    SeatMatrix() class is used to print the seat matrix based upon the CLASS provided.
    """

    def __init__(self, business_rows, economy_rows):
        self.brow = business_rows
        self.erow = economy_rows

    def matrix(self, category):
        self.category = category

        business = ['A', 'B', 'C', 'D']
        economy = ['A', 'B', 'C', 'D', 'E', 'F']
        option = True
        while option:
            print("\nSeat Matrix:")
            if self.category.upper() == "BUSINESS":
                option = False
                print('\nBusiness Class')
                for j in range(1, self.brow + 1):
                    print(
                        f"{str(j) + business[0] : >5} {str(j) + business[1] : >9}"
                        f" {str(j) + business[2] : >8} {str(j) + business[3] : >9}")

            elif self.category.upper() == "ECONOMY":
                option = False
                print('\nEconomy Class')
                for j in range(self.brow + 1, self.brow + self.erow + 1):
                    print(
                        f"{str(j) + economy[0] : >5} {str(j) + economy[1] : >5} {str(j) + economy[2] : >5}"
                        f" {str(j) + economy[3] : >5}{str(j) + economy[4] : >5} {str(j) + economy[5] : >5}")

            else:
                print("Invalid class enter.\nTry again: ")
                self.category = input("Enter Class: ")
                continue




###################################################################################################


class Seats(object):
    """
    Seats() class is used for creation of seats in Business class and Economy class.
    This class also divides each seat into category --> window, middle, aisle
    """

    def __init__(self,  business_rows, economy_rows):
        self.brow = int(business_rows)
        self.erow = int(economy_rows)
        self.economy_seats = list()
        self.business_seats = list()
        self.window_seats = list()
        self.aisle_seats = list()
        self.middle_seats = list()

    # separated seat into window, middle and aisle
    def category(self):
        for i in range(1, self.brow+1):
            self.business_seats.append([str(i) + 'A', str(i) + 'B', str(i) + 'C', str(i) + 'D'])

        for row in self.business_seats:
            for seat in row:
                if 'A' in seat or 'D' in seat:
                    self.window_seats.append(seat)
                else:
                    self.aisle_seats.append(seat)

        for i in range(self.brow + 1, self.brow + self.erow + 1):
            self.economy_seats.append([str(i) + 'A', str(i) + 'B', str(i) + 'C',
                                  str(i) + 'D', str(i) + 'E', str(i) + 'F'])

        for row in self.economy_seats:
            for seat in row:
                if 'A' in seat or 'F' in seat:
                    self.window_seats.append(seat)
                elif 'C' in seat or 'D' in seat:
                    self.aisle_seats.append(seat)
                else:
                    self.middle_seats.append(seat)

        return self.window_seats,  self.middle_seats, self.aisle_seats,

###################################################################################################

class SeatBooking():
    """
    SeatBooking() class is used to book seats in flight.
    This contans 2 function --> bookseat() and vacantseat()
    bookseat() return true if seat is available and allocates this seat to passenger
    vacantseat() dumps the available seats into available_seat.pkl file.
    """

    def __init__(self):
        with open("available_seat.pkl", "rb") as available:
            seats = pickle.load(available)
            self.window_seats = seats['window']
            self.middle_seats = seats['middle']
            self.aisle_seats = seats['aisle']

    def bookseat(self,seat):
        self.seat = seat
        if self.seat in self.aisle_seats:
            self.aisle_seats.remove(self.seat)
            return True
        if self.seat in self.window_seats:
            self.window_seats.remove(self.seat)
            return True
        if self.seat in self.middle_seats:
            self.middle_seats.remove(self.seat)
            return True
        else:
            return False

    def vacantseat(self):
        with open('available_seat.pkl', 'wb') as available:
            seats = dict()
            seats['window'] = self.window_seats
            seats['middle'] = self.middle_seats
            seats['aisle']= self.aisle_seats
            pickle.dump(seats, available)

###################################################################################################

class Passenger_info(Generate):
    """
    This class is used to print the ticket of the passenger.
    This class contains information about passenger that needs to be stored in server.
    """

    # initialising the passenger information
    def __init__(self, name, age, email, seat,category, source, destination):
        super(Passenger_info, self).__init__(source, destination)
        self.name = name
        self.age = age
        self.email = email
        self.source = source
        self.destination = destination
        self.seat = seat
        self.category = category

    # ticket() is used to print the ticket for passenger
    def ticket(self, book_id):
        self.book_id = book_id
        print('=' * 60)
        print("Name : {}".format(self.name))
        print("Age : {}              Email : {}".format(self.age, self.email))
        print("Seat : {}             Class : {}".format(self.seat, self.category))
        print("Source : {}       Destination : {}".format(self.source, self.destination))
        print("Booking ID : {}".format(self.book_id))
        print("Booking Date : {}".format(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        print('=' * 60)
        close = input('Press q to exit: ')

    # storeData() used to store data into pickle file
    def storeData(self, book_id):
        self.book_id = book_id

        with open("passengers_data.pkl", 'rb') as passenger_data:
            passengers = pickle.load(passenger_data)

        passengers[self.book_id] = {self.name,self.age, self.email, self.source, self.destination, self.seat, self.category}

        with open("passengers_data.pkl", 'wb') as passenger_data:
            pickle.dump(passengers, passenger_data)
