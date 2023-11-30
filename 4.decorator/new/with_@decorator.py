# Base component function
def simple_coffee_cost():
    return 2


def simple_coffee_description():
    return "Simple coffee"


# Decorator function
def add_milk(func):
    def wrapper():
        return func() + 1

    return wrapper


def add_whip(func):
    def wrapper():
        return func() + 0.5

    return wrapper


def add_milk_desc(func):
    def wrapper():
        return func() + ", with milk"

    return wrapper

def add_whip_desc(func):
    def wrapper():
        return func() + ", with whip"

    return wrapper

# Usage
@add_milk
def milk_coffee_cost():
    return simple_coffee_cost()


@add_milk_desc
def milk_coffee_description():
    return simple_coffee_description() 


@add_whip
def whip_coffee_cost():
    return milk_coffee_cost()


@add_whip_desc
def whip_coffee_description():
    return milk_coffee_description() 


print(f"Cost: ${simple_coffee_cost()}, Description: {simple_coffee_description()}")
print(f"Cost: ${milk_coffee_cost()}, Description: {milk_coffee_description()}")
print(f"Cost: ${whip_coffee_cost()}, Description: {whip_coffee_description()}")
