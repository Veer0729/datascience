# # BASIC CLASS DEFINITION (ENCAPSULATION)
# class Car:
#     total = 0  # Class variable (shared by all instances)
    
#     # CONSTRUCTOR WITH PRIVATE ATTRIBUTES (ENCAPSULATION)
#     def __init__(self, brand, model):
#         self.__brand = brand  # Private attribute (double underscore)
#         self.__model = model  # Private attribute
#         Car.total += 1  # Modifying class variable
    
#     # INSTANCE METHOD
#     def fullname(self):
#         return f"{self.__brand} {self.__model}"
    
#     # GETTER METHOD (ENCAPSULATION)
#     def get_brand(self):
#         return self.__brand + "!"
    
#     # METHOD (LATER OVERRIDDEN IN CHILD CLASS - POLYMORPHISM)
#     def fuel_type(self):
#         return "Petrol/Diesel car"
    
#     # STATIC METHOD
#     @staticmethod
#     def general_description():
#         return "Cars are means of transport"
    
#     # PROPERTY DECORATOR (GETTER)
#     @property
#     def model(self):
#         return self.__model


# # INHERITANCE (SINGLE INHERITANCE)
# class ElectricCar(Car):  # Inherits from Car class
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)  # Calling parent constructor
#         self.battery_size = battery_size  # New attribute
    
#     # METHOD OVERRIDING (POLYMORPHISM)
#     def fuel_type(self):
#         return "Electric Car"  # Overrides parent implementation


# # MULTIPLE INHERITANCE
# class Battery:
#     def info(self):
#         return "this is a battery"

# class Engine:
#     def info1(self):
#         return "this is an engine"

# class Newcar(Battery, Engine):  # Inherits from multiple classes
#     pass  # Inherits methods from both parents

# electric = ElectricCar("tesla", "model S", "390kwh")
# print(electric.fullname())
# print(electric.battery_size)

# safari = Car("tata", "safari")
# tesla = ElectricCar("tesla", "model S", "390kwh")
# print(isinstance(tesla, Car))
# print(isinstance(tesla, ElectricCar))
# print(safari.fuel_type())
# print(tesla.fuel_type())
# print(Car.total)
# print(Car.general_description())
# print(Car.model)

# def decorate(func):
#     def wrapper(a, b):
#         print("addition is: ")
#         func(a, b)
#         print("done")
#     return wrapper


# @decorate
# def addition(a, b):
#     print(f"addition of both number are: {a+b}")

# addition(12, 56)

# def addition(*a):
#     sum = 0
#     for i in a:
#         sum = sum + i

#     print(sum)

# addition(12,56,34,456,3423,5,435345,23432,89)

# compershion

l = [i for i in range(1, 21) if i % 2 == 0]
print(l)

l = {i: i**2 for i in range(1, 21)}
print(l)

addition = lambda a : "even" if a%2 == 0 else "odd"
print(addition(34))

a = [2,5,6,7,9]

result = map(lambda x: x*2, a)
print(list(result))

result1 = filter(lambda x: True if a%2 == 0 else False, a)
print(list(result1))