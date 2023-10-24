class Vehicle:
    def start_engine(self):
        return "Vehicle engine started"

    def stop_engine(self):
        return "Vehicle engine stopped"


class Car(Vehicle):
    def __init__(self, max_speed, current_speed=0):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        self.current_speed = 0
        return "Car engine stopped"


class SportCar(Car):
    def start_engine(self):
        parent_result = super().start_engine()
        return f"{parent_result}, Max Speed: {self.max_speed}"

    def stop_engine(self):
        parent_result = super().stop_engine()
        return f"{parent_result}, Current Speed: {self.current_speed}"


car = SportCar(max_speed=200)
print(car.start_engine()) 
print(car.stop_engine())   
