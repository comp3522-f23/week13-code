# Base component interface
class Coffee:
    def cost(self):
        pass

    def description(self):
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 2

    def description(self):
        return "Simple coffee"


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete decorators
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ", with milk"


class Whip(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 0.5

    def description(self):
        return self._coffee.description() + ", with whipped cream"


# Usage
simple_coffee = SimpleCoffee()
print(f"Cost: ${simple_coffee.cost()}, Description: {simple_coffee.description()}")

milk_coffee = Milk(simple_coffee)
print(f"Cost: ${milk_coffee.cost()}, Description: {milk_coffee.description()}")

whip_coffee = Whip(milk_coffee)
print(f"Cost: ${whip_coffee.cost()}, Description: {whip_coffee.description()}")
