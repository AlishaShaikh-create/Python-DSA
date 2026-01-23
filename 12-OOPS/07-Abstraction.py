from abc import ABC,abstractmethod

# Abstract class
class Vehicle(ABC):
    def drive(self):
        print("the vehicle is used for driving")
    
    @abstractmethod   
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")  
        
def operate_vehicle(vehicle):
    return vehicle.start_engine() , vehicle.drive()


c1=Car()
operate_vehicle(c1)        