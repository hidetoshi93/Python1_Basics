# object oriented programming

class Car():
    # ClassVariable
    tax = 1

    def __init__(self, brand, model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price

    def Brand(self):
        return self.brand

    def GetValue(self):
        self.tax = 0.5
        # tax = 0.75
        return(self.price * Car.tax)

car_1 = Car("Vinfast", "LuxA", 2017, 1000)
car_2 = Car("BMW", "i320", 1916, 700)

print(f"{car_1.model} of the price is {car_1.GetValue()}")
print(f"{car_2.model} of the price is {car_2.GetValue()}")
print(Car.tax)
print(car_1.tax)