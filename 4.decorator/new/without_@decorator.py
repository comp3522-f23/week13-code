# Base component functions
def simple_coffee_cost():
    return 2


def simple_coffee_description():
    return "Simple coffee"


# Decorator functions
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


# Usage without decorators
milk_coffee_cost = add_milk(simple_coffee_cost)
milk_coffee_description = add_milk_desc(simple_coffee_description)
whip_coffee_cost = add_whip(milk_coffee_cost)
whip_coffee_description = add_whip_desc(milk_coffee_description)

print(f"Cost: ${simple_coffee_cost()}, Description: {simple_coffee_description()}")
print(f"Cost: ${milk_coffee_cost()}, Description: {milk_coffee_description()}")
print(f"Cost: ${whip_coffee_cost()}, Description: {whip_coffee_description()}")
