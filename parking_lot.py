from abc import ABC, abstractmethod
from enum import Enum
# Requirements:-

# R1: The parking lot should have the capacity to park 40,000 vehicles.
# R2: The four different types of parking spots are handicapped, compact, large, and motorcycle.
# R3: The parking lot should have multiple entrance and exit points.
# R4: Four types of vehicles should be allowed to park in the parking lot, which are as follows:
    # Car
    # Truck
    # Van
    # Motorcycle

# R5: The parking lot should have a display board that shows free parking spots for each parking spot type.
# R6: The system should not allow more vehicles in the parking lot if the maximum capacity (40,000) is reached.
# R7: If the parking lot is completely occupied, the system should show a message on the entrance and on the parking lot display board.
# R8: Customers should be able to collect a parking ticket from the entrance and pay at the exit.
# R9: The customer can pay for the ticket either with an automated exit panel or pay the parking agent at the exit.
# R10: The payment should be calculated at an hourly rate.
# R11: Payment can be made using either a credit/debit card or cash.


class Vehicle(ABC):
    def __init__(self,license_no) -> None:
        self.license_no=license_no

    @abstractmethod
    def assign_ticket(self):
        pass

class Car(Vehicle):

    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self,ticket):
        pass

class Van(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self,ticket):
        pass

class Truck(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self,ticket):
        pass

class Motorcycle(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self,ticket):
        pass


class ParkingSpot(ABC):
    def __init__(self,id,isFree) -> None:
        self.id=id
        self.isFree=isFree

    @abstractmethod
    def getIsFree(self):
        pass

class Large(ParkingSpot):
    def __init__(self, id, isFree) -> None:
        super().__init__(id, isFree)
    
    def getIsFree(self):
        pass

class Handicapped(ParkingSpot):
    def __init__(self, id, isFree) -> None:
        super().__init__(id, isFree)
    
    def getIsFree(self):
        pass
class Motorcycle(ParkingSpot):
    def __init__(self, id, isFree) -> None:
        super().__init__(id, isFree)
    
    def getIsFree(self):
        pass

class Compact(ParkingSpot):
    def __init__(self, id, isFree) -> None:
        super().__init__(id, isFree)
    
    def getIsFree(self):
        pass

class AccountStatus(Enum):
    blocked="BLOCKED"
    active="ACTIVE"
    deleted="DELETED"

class Person:
    def __init__(self,name,dob,email,phone) -> None:
        self.name=name
        self.dob=dob
        self.email=email
        self.phone=phone
class Account(ABC):
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password
        self.status=AccountStatus

    @abstractmethod
    def resetPassword(self):
        pass


class Admin(Account):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
    
    def addParkingSpot(self):
        pass

    def updateParkingBoard(self):
        pass

class ParkingAgent(Account):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
    
    def processTicket(self):
        pass


class ParkingBoard():
    def __init__(self) -> None:
        self.parkingMap={}
    
    def addParkingSpot(self):
        pass

    def showFreeParkingSpot(self):
        pass

class Ticket():
    def __init__(self,id,amount,timestamp,parkingSpot) -> None:
        self.id=id
        self.amount=amount
        self.timestamp=timestamp
        self.parkingSpot=parkingSpot

class Entrance():
    def __init__(self) -> None:
        self.ticket=Ticket
    
    def collectParkingTicket(self):
        return self.ticket

class Exit():
    def __init__(self) -> None:
        pass
    def validateTicket(self):
        pass

class PaymentStatus(Enum):
    SUCCESS="success"
    FAILED="failed"
    DECLINED="declined"
    REFUNDED="refunded"
class Payment(ABC):
    def __init__(self,amount,timestamp) -> None:
        self.amount=amount
        self.timestamp=timestamp
        self.status=PaymentStatus
    
    @abstractmethod
    def makePayment(self):
        pass



class ParkingRate():
    def __init__(self,hours,rate) -> None:
        self.hours=hours
        self.rate=rate
    
    def calculate(self):
        pass

class Address():
    def __init__(self,address,zipcode,city,state,country) -> None:
        self.address=address
        self.zipcode=zipcode
        self.city=city
        self.state=state
        self.country=country
class ParkingLot():
    def __init__(self,id,name,address) -> None:
        self.id=id
        self.name=name
        self.address=Address
    
    def addEntrance(self):
        pass
    
    def addExit(self):
        pass
    
    def getParkingTicket(self):
        pass
    
