import main
from tkinter import *
from tkinter import ttk
import functools

class Vehicle:
    def start_moving(self):
        print("We moving!")
    def stop_moving(self):
        print("we're not moving")

class VehicleFactory:
    def create_vehicle(self):
        print("Vehicle created")
        return Vehicle()

class car(Vehicle):
    engine = "2.0L"
    fuel = 100
    def refuel(self):
        fuel = 100

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        print("Car created")
        return car()

class electric_bike(Vehicle):
    engine = "200KW"
    battery = 100
    def recharge(self):
        battery = 100

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        print("Bike created")
        return electric_bike()


class Client:
    def __init__(self, factory: VehicleFactory):
        print("Client: creating vehicle")
        self.Vehicle = factory.create_vehicle()

    def get_vehicle(self):
        return self.Vehicle

def create_bike():
    bike_factory = BikeFactory()
    bike_factory_client = Client(bike_factory)
    vehicle = bike_factory_client.get_vehicle()
    print("Got vehicle of object type: " + str(vehicle))

def create_car():
    car_factory = CarFactory()
    car_factory_client = Client(car_factory)
    vehicle = car_factory_client.get_vehicle()
    print("Got vehicle of object type: " + str(vehicle))


def init_window(main_window):
    window = main.Window("Builder design pattern", 30, 100)
    window.add_back_button()
    window.add_title("Window Design Pattern", 1, 1)
    bike_button = ttk.Button(window, text="Create bike", command=create_bike)
    bike_button.grid(row=2, column=1)
    car_button = ttk.Button(window, text="Create bike", command=create_car)
    car_button.grid(row=3, column=1)
    window.parent = main_window


