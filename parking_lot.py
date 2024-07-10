import datetime
import math

class Vehicle:
    def __init__(self,spot_size):
        self.spot_size = spot_size
    
    def getSpotSize(self):
        return self.spot_size

class Driver:
    def __init__(self,id,vehicle):
        self.vehicle = vehicle
        self.id = id
        self.due_amount=0
    
    def getVehicle(self):
        return self.vehicle

    def getId(self):
        return self.id

    def charge(self,amount):
        self.due_amount +=amount

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__(1)

class Limo(Vehicle):
    def __init__(self):
        super(Limo, self).__init__(2)

class Truck(Vehicle):
    def __init__(self):
        super(Truck, self).__init__(3)

class ParkingFloor:
    def __init__(self,spot_count):
        self.spots=[0]*spot_count
        self.vehicle_map={}
    
    def parkVehicle(self,vehicle):
        spot_size=vehicle.getSpotSize()
        l,r=0,0

        while r<len(self.spots):
            if self.spots[r]!=0:
                l=r+1
            if r-l+1==spot_size:

                for i in range(l,r+1):
                    self.spots[i]=1
                self.vehicle_map[vehicle]=[l,r]
                return True
            r+=1
        return False
    
    def removeVehicle(self,vehicle):
        l,r=self.vehicle_map[vehicle]

        for i in range(l,r+1):
            self.spots[i]=0
        del self.vehicle_map[vehicle]
    

    def getParkingSpots(self):
        return self.spots

    def getVehicleSpots(self,vehicle):
        return self.vehicle_map[vehicle]


class ParkingGarage:
    def __init__(self,floorCount,spotsPerFloor) -> None:
        self.parkings=[ParkingFloor(spotsPerFloor) for _ in floorCount]
    
    def parkVehicle(self,vehicle):

        for parking in self.parkings:
            if parking.parkVehicle(vehicle):
                return True
        return False
    
    def removeVehicle(self,vehicle):

        for parking in self.parkings:
            if parking.getVehicleSpots(vehicle):
                parking.removeVehicle(vehicle)
                return True
        return False


class ParkingSystem:
    def __init__(self,parking_garage,hourly_rate):
        self.parking_garage=parking_garage
        self.hourly_rate=hourly_rate
        self.time_parked={}
    
    def parkVehicle(self,driver):
        vehicle=driver.getVehicle()
        current_hour=datetime.datetime.now().hour
        isParked=self.parking_garage.parkVehicle(vehicle)
        if isParked:
            self.time_parked[driver.getId()]=current_hour
        return isParked

    def removeVehicle(self,driver):
        current_hour=datetime.datetime.now().hour
        timeperiod=math.ceil(current_hour-self.time_parked[driver.getId()])
        driver.charge(timeperiod*self.hourly_rate)
        del self.time_parked[driver.getId()]
        return self.parking_garage.remove_vehicle(driver.getVehicle())
        








