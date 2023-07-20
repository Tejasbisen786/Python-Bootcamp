# here Definig the Parent Class or base Class  i.e Vehicle

class Vehicle:
    def __init__(self, brand, model):
        # self.brand = brand        encapusulate the input 
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"     



# here car is child clas of vehicle and it act like derived 
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)     # Accesing the Base Class attribute using Super Keyword
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Car, Number of Doors: {self.num_doors}"

# bike is dervied class 
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Bike, Bike Type: {self.bike_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, payload_capacity):
        super().__init__(brand, model)
        self.payload_capacity = payload_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Type: Truck, Payload Capacity: {self.payload_capacity} kg"


#   Creating bject of a Class That is defined above and pssing the value 
    car1 = Car("Toyota", "Camry", 4)
    bike1 = Bike("Honda", "CBR 1000RR", "Sports")
    truck1 = Truck("Ford", "F-150", 3000)

    print(car1.display_info())
    print(bike1.display_info())
    print(truck1.display_info())


