# Existing code for Item, Toy, StuffedAnimal, Candy classes and ItemFactory remains unchanged


class Item:
    def __init__(self, item) -> None:
        self.product_id = item["product_id"]
        self.name = item["item_name"]
        self.description = item["description"]
        self.quantity = item["quantity"]
        self.order_number = item["order_number"]
        self.holiday_type = item["holiday_type"]
        self.item_type = item["item_type"]

    def reduce_quantity(self, amount: int):
        self.quantity -= amount

    def order_more(self):
        """
        # In the event the store receives an order for an item that it does not have inventory for, then it should go ahead and get a 100 of those items made by the corresponding factory class.
        """
        self.quantity += 100

    def __str__(self):
        return f"Item: {self.name} ({self.product_id} - {self.quantity})"


class HolidayStore:
    def __init__(self) -> None:
        self.inventory: list[Item] = []  # inventory of items

    def process_web_orders(self, order):
        for item in self.inventory:
            if item.product_id == order.product_id:
                if order.quantity > item.quantity:
                    item.order_more()
                item.reduce_quantity(order.quantity)
                return

        # if we get here, we don't have the item in stock
        # so we need to order more
        self.inventory.append(ItemFactory.create_item(order))

    def check_inventory(self):
        """
                Check Inventory This allows the store owner to check what is currently in stock and will also provide a status indicator for items if the stock for this item is LOW , VERY LOW , IN STOCK, or OUT OF STOCK. Print a list of all the items, their information, and the stock status indicator

        In Stock - 10 or more items in stock
        Low - Less than 10 items
        Very Low - Less than 3 items
        Out of Stock - 0 items
        Exit
        """
        for item in self.inventory:
            if item.quantity >= 10:
                print(f"{item} - In Stock")
            elif item.quantity < 10 and item.quantity > 3:
                print(f"{item} - Low")
            elif item.quantity <= 3 and item.quantity > 0:
                print(f"{item} - Very Low")
            else:
                print(f"{item} - Out of Stock")

    def create_daily_transaction_report(self):
        """
                # **Daily Transaction Report**

        # When the user chooses to exit the program, the program should write the Daily Transaction Report to a text file. The file specifies the list of orders processed that day.

        # The text file should follow the naming convention DTR\_DDMMYY\_HHMM.txt where DDMMYY refers to the date, month and year (for example, 19th Feb 2020 would be 190220) and HHMM refers to the hour and minute (for example 1:30pm would be 1330).

        # Be sure to follow the formatting in the example below:

        # ```
        # HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)

        # 05-03-2020 17:58

        # Order 102, Item StuffedAnimal, Product ID H9405S, Name "Skelly the Tap Dancer", Quantity 3

        # Order 103, Item Toy, Product ID T2134C, Name "Santas Workshop Deluxe Edition", Quantity 20

        # Order 104, Item Toy, Product ID T3243H, Name "Terrifying Tarantula", Quantity 17

        # Order 105, Could not process order data was corrupted, InvalidDataError - Stuffing can only be "Polyester Fibrefill" or "Wool"
        # ```"""

        # write to a file
        # get DDMMYY_HHMM
        now = datetime.now()
        formatted_date_time = now.strftime("%d%m%y_%H%M")
        DDMMYY_HHMM = formatted_date_time
        with open(f"DTR_{DDMMYY_HHMM}.txt", "w") as f:
            f.write("HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n")
            f.write("05-03-2020 17:58\n")
            for item in self.inventory:
                f.write(
                    f"Order {item.order_number}, Item {item.item_type}, Product ID {item.product_id}, Name {item.name}, Quantity {item.quantity}\n"
                )
            f.close()


# Toy (Abstract Class, extends Item):
# Attributes:
# is_battery_operated: bool
# recommended_age: int
# Methods:
# (Abstract) specific_method() # To be implemented in each concrete toy
class Toy(Item):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.is_battery_operated = item.get(
            "is_battery_operated", False
        )
        self.recommended_age = item.get("recommended_age", 0)

    def specific_method(self):
        pass


# StuffedAnimal (Abstract Class, extends Item):
# Attributes:
# stuffing: str
# size: str
# fabric: str
# has_glow_in_dark: bool
# Methods:
# (Abstract) specific_method() # To be implemented in each concrete stuffed animal
class StuffedAnimal(Item):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.stuffing = item.get("stuffing", "")
        self.size = item.get("size", "")
        self.fabric = item.get("fabric", "")
        self.has_glow_in_dark = item.get("has_glow_in_dark", False)

    def specific_method(self):
        pass


# Candy (Abstract Class, extends Item):
# Attributes:
# contains_nuts: bool
# lactose_free: bool
# Methods:
# (Abstract) specific_method() # To be implemented in each concrete candy
class Candy(Item):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.contains_nuts = item.get("contains_nets", False)
        self.lactose_free = item.get("lactose_free", False)

    def specific_method(self):
        pass


# Attributes:
# ChristmasToy (Concrete Class, extends Toy):
# dimensions: Tuple[int, int]
# num_rooms: int


class ChristmasToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.dimensions = item.get("dimensions", (0, 0))
        self.num_rooms = item.get("num_rooms", 0)


# HalloweenToy (Concrete Class, extends Toy):
# Attributes:
# speed: int
# jump_height: int
# glows_in_dark: bool
# spider_type: str


class HalloweenToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.speed = item.get("speed", 0)
        self.jump_height = item.get("height", 0)
        self.glows_in_dark = item.get("glows_in_dark", False)
        self.spider_type = item.get("spider_type", "")


# EasterToy (Concrete Class, extends Toy):
# Attributes:
# num_sound_effects: int
# color: str


class EasterToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.num_sound_effects = item.get("num_sound_effects", 0)
        self.color = item.get("color", "")


# DancingSkeleton (Concrete Class, extends StuffedAnimal):
# (No additional attributes)
class DancingSkeleton(StuffedAnimal):
    def __init__(self, item) -> None:
        super().__init__(item)


# Reindeer (Concrete Class, extends StuffedAnimal):
# Attributes:
# has_glow_in_dark_nose: bool
class Reindeer(StuffedAnimal):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.has_glow_in_dark_nose = item.get(
            "has_glow_in_dark_nose", False
        )


# EasterBunny (Concrete Class, extends StuffedAnimal):
# Attributes:
# color: str
class EasterBunny(StuffedAnimal):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.color = item.get("color", "")


# PumpkinCaramelToffee (Concrete Class, extends Candy):
# Attributes:
# variety: str
class PumpkinCaramelToffee(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.variety = item.get("variety", "")


# CandyCanes (Concrete Class, extends Candy):
# Attributes:
# color_stripes: str
class CandyCanes(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.color_stripes = item.get("color_stripes", "")


# CremeEggs (Concrete Class, extends Candy):
# Attributes:
# pack_size: int
class CremeEggs(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.pack_size = item.get("pack_size", 0)


def create_christmas_toy(item):
    return ChristmasToy(item)


def create_christmas_stuffed_animal(item):
    return Reindeer(item)


def create_christmas_candy(item):
    return CandyCanes(item)


def create_halloween_toy(item):
    return HalloweenToy(item)


def create_halloween_stuffed_animal(item):
    return DancingSkeleton(item)


def create_halloween_candy(item):
    return PumpkinCaramelToffee(item)


def create_easter_toy(item):
    return EasterToy(item)


def create_easter_stuffed_animal(item):
    return EasterBunny(item)


def create_easter_candy(item):
    return CremeEggs(item)


class ItemFactory:
    factories = {
        "Christmas": {
            "Toy": create_christmas_toy,
            "StuffedAnimal": create_christmas_stuffed_animal,
            "Candy": create_christmas_candy,
        },
        "Halloween": {
            "Toy": create_halloween_toy,
            "StuffedAnimal": create_halloween_stuffed_animal,
            "Candy": create_halloween_candy,
        },
        "Easter": {
            "Toy": create_easter_toy,
            "StuffedAnimal": create_easter_stuffed_animal,
            "Candy": create_easter_candy,
        },
    }

    @staticmethod
    def create_item(item) -> Item:
        holiday = item["holiday_type"]
        item_type = item["item_type"]
        if holiday in ItemFactory.factories:
            if item_type in ItemFactory.factories[holiday]:
                return ItemFactory.factories[holiday][item_type](item)
            else:
                raise ValueError(f"Invalid item type: {item_type}")
        else:
            raise ValueError(f"No factory registered for holiday: {holiday}")


# Assume the classes and refactored factory functions are defined here

# Example item details
christmas_toy_details = {
    "product_id": "CT001",
    "item_name": "Santa's Sleigh",
    "description": "A magical sleigh for Christmas!",
    "quantity": 50,
    "order_number": "ORD123",
    "holiday_type": "Christmas",
    "item_type": "Toy",
    "product_details": {"dimensions": (10, 5), "num_rooms": 1},
}

halloween_candy_details = {
    "product_id": "HC001",
    "item_name": "Spooky Candies",
    "description": "Deliciously scary candies!",
    "quantity": 100,
    "order_number": "ORD456",
    "holiday_type": "Halloween",
    "item_type": "Candy",
    "product_details": {"variety": "Assorted flavors"},
}

easter_stuffed_animal_details = {
    "product_id": "EA001",
    "item_name": "Easter Chick",
    "description": "A fluffy Easter chick!",
    "quantity": 30,
    "order_number": "ORD789",
    "holiday_type": "Easter",
    "item_type": "StuffedAnimal",
    "product_details": {"color": "Yellow"},
}


# Creating items using the ItemFactory
def create_and_print_item(item_details):
    created_item = ItemFactory.create_item(item_details)
    print(f"Created: {created_item}")


create_and_print_item(christmas_toy_details)
create_and_print_item(halloween_candy_details)
create_and_print_item(easter_stuffed_animal_details)
