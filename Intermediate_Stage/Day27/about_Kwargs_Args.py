# Lesson on Unlimited Positional Argument *args, and
# Unlimited Keyword Argument **kwargs

def add(*args):
    return sum(args)


x = add(1, 2, 4, 5, 6, 7, 8)
print(x)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(4, add=3, multiply=5, subtract=10)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)