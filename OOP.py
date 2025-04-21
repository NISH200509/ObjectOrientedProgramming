from abc import ABC, abstractmethod

class carfactory(ABC):

    @abstractmethod #every subclass must define this method, or you’re not allowed to create objects from it
    def drive(self):
        pass

    @abstractmethod
    def pitstop(self):
        pass



class GPinfo(object):
    year = 2022
    grand_prix = "Sao Paulo"
    num_drivers = 0


class Car(GPinfo, carfactory): 
    #inherit from GPinfo class and carfactory class (multiple inheritance)

    #multilevel inheritance is also possible Car <- GPinfo <- carfactory
    #                      can think of as   son <- father <- grandfather
    def __init__(self, driver, team, car_name):
        self.driver = driver
        self.team = team
        self.car_name = car_name
        Car.num_drivers += 1
        
    def drive(self):
        print(f"{self.driver} of {self.team} is now driving.")

    def pitstop(self):
        print(f"{self.driver} of {self.team} has stopped for a pitstop.")

    def describe(self):
        print( f"{self.driver} is from {self.team} and hes driving {self.car_name}")
    
car1= Car("Lewis Hamilton", "Mercedes", "W11")
car2= Car("Max Verstappen", "Red Bull", "RB16") 
car3= Car("Charles Leclerc", "Ferrari", "SF71H")
car4= Car("Sebastian Vettel", "Aston Martin", "AMR23")
car5= Car("Lando Norris", "McLaren", "MCL35M")


#its good practice to access the class variable by the class name itself
#print(car1.grand_prix)     #but we can also access it by the instance of the class

if Car.num_drivers > 1:
    print(f"We're in {Car.grand_prix} and the year is {Car.year} and {Car.num_drivers} drivers are fighting for the championship")
else:
    print(f"We're in {Car.grand_prix} and the year is {Car.year} and {Car.num_drivers} driver are fighting for the championship")


Teams = [car1, car2, car3, car4, car5]

for car in Teams:
    car.drive()


