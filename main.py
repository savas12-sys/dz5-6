class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self):
        if not self.is_running:
            print("Engine started")
            self.is_running = True
        else:
            print("Engine is already running")

    def stop(self):
        if self.is_running:
            print("Engine stopped")
            self.is_running = False
        else:
            print("Engine is already stopped")

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def start_engine(self):
        if self.engine:
            self.engine.start()
        else:
            print("No engine installed")

    def stop_engine(self):
        if self.engine:
            self.engine.stop()
        else:
            print("No engine installed")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def display_info(self):
        super().display_info()
        print(f"Bike type: {self.bike_type}")

# Приклад використання класів
car_engine = Engine("gasoline")
car = Car("Toyota", "Camry", 2022, 4)
car.set_engine(car_engine)

bike_engine = Engine("petrol")
bike = Bike("Honda", "CBR1000RR", 2022, "sport")
bike.set_engine(bike_engine)

car.display_info()
car.start_engine()
car.stop_engine()

print()

bike.display_info()
bike.start_engine()
bike.stop_engine()