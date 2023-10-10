class Car:
    def __init__(self, brand, model, production_year, color, horse_power, is_sports_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sports_car = is_sports_car

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_production_year(self):
        return self.__production_year

    def get_color(self):
        return self.__color

    def get_horse_power(self):
        return self.__horse_power

    def is_sports_car(self):
        return self.__is_sports_car

    def change_color(self, new_color):
        if self.__color != new_color:
            self.__color = new_color
            print("Color change successful.")
            return True
        else:
            print("The car is already the same color as the new color.")
            return False

    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        else:
            return False
    def increase_horse_power(self, hp):
        if hp > 0:
            self.__horse_power += hp
            return True
        else:
            return False
        
my_car = Car("Toyota", "Camry", 2020, "Blue", 180)

print("Brand:", my_car.get_brand())
print("Model:", my_car.get_model())
print("Production Year:", my_car.get_production_year())
print("Color:", my_car.get_color())
print("Horsepower:", my_car.get_horse_power())
print("Is Sports Car:", my_car.is_sports_car())

print(my_car.change_color("Red"))  
print(my_car.change_color("Blue"))  

print(my_car.increase_horse_power(20)) 
print("Horsepower after increase:", my_car.get_horse_power()) 

print(my_car.increase_horse_power(-10)) 
print("Horsepower after unsuccessful increase:", my_car.get_horse_power())  