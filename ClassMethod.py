from types import ClassMethodDescriptorType, MethodDescriptorType


# ClassMethod
# StaticMethod

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
    # Regular Method
    def Get_Value(self):
        self.tax = 0.5
        # tax = 0.75
        return(self.price * Car.tax)

    # Class Method
    @classmethod
    def Set_Tax(cls):
        cls.tax = 1.5

car_1 = Car("Vinfast", "LuxA", 2017, 1000)
car_2 = Car("BMW", "i320", 1916, 700)

print(Car.tax)
print(f"{car_1.model} of the price is {car_1.Get_Value()}")
car_1.Set_Tax()
print(f"{car_2.model} of the price is {car_2.Get_Value()}")
print(Car.tax)
print(car_1.tax)