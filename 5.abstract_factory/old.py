import pandas as pd


from datetime import datetime


# Item: (Abstract Class)
# Attributes:
# product_id: str
# name: str
# description: str
# quantity: int
# factory: AbstractFactory
# Methods:
# reduce_quantity(amount: int)
# order_more()
class Item:
    def __init__(self, item) -> None:
        self.product_id = item.product_id
        self.name = item.item_name
        self.description = item.description
        self.quantity = item.quantity
        self.order_number = item.order_number
        item.holiday_type = item.holiday_type
        self.item_type = item.item_type

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
        self.is_battery_operated = item.product_details.get("is_battery_operated", False)
        self.recommended_age = item.product_details.get("recommended_age", 0)

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
        self.stuffing = item.product_details.get("stuffing", "")
        self.size = item.product_details.get("size", "")
        self.fabric = item.product_details.get("fabric", "")
        self.has_glow_in_dark = item.product_details.get("has_glow_in_dark", False)

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
        self.contains_nuts = item.product_details.get("contains_nets", False)
        self.lactose_free = item.product_details.get("lactose_free", False)

    def specific_method(self):
        pass


# Attributes:
# ChristmasToy (Concrete Class, extends Toy):
# dimensions: Tuple[int, int]
# num_rooms: int


class ChristmasToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.dimensions = item.product_details.get("dimensions", (0, 0))
        self.num_rooms = item.product_details.get("num_rooms", 0)


# HalloweenToy (Concrete Class, extends Toy):
# Attributes:
# speed: int
# jump_height: int
# glows_in_dark: bool
# spider_type: str


class HalloweenToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.speed = item.product_details.get("speed", 0)
        self.jump_height = item.product_details.get("height", 0)
        self.glows_in_dark = item.product_details.get("glows_in_dark", False)
        self.spider_type = item.product_details.get("spider_type", "")


# EasterToy (Concrete Class, extends Toy):
# Attributes:
# num_sound_effects: int
# color: str


class EasterToy(Toy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.num_sound_effects = item.product_details.get("num_sound_effects", 0)
        self.color = item.product_details.get("color", "")


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
        self.has_glow_in_dark_nose = item.product_details.get("has_glow_in_dark_nose", False)


# EasterBunny (Concrete Class, extends StuffedAnimal):
# Attributes:
# color: str
class EasterBunny(StuffedAnimal):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.color = item.product_details.get("color", "")


# PumpkinCaramelToffee (Concrete Class, extends Candy):
# Attributes:
# variety: str
class PumpkinCaramelToffee(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.variety = item.product_details.get("variety", "")


# CandyCanes (Concrete Class, extends Candy):
# Attributes:
# color_stripes: str
class CandyCanes(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.color_stripes = item.product_details.get("color_stripes", "")


# CremeEggs (Concrete Class, extends Candy):
# Attributes:
# pack_size: int
class CremeEggs(Candy):
    def __init__(self, item) -> None:
        super().__init__(item)
        self.pack_size = item.product_details.get("pack_size", 0)


# AbstractFactory:
# Methods:
# create_toy()
# create_stuffed_animal()
# create_candy()
class AbstractFactory:
    def create_toy(self):
        pass

    def create_stuffed_animal(self):
        pass

    def create_candy(self):
        pass


# ChristmasFactory (Concrete Class, extends AbstractFactory):
# Methods:
# (Implement create methods for Christmas-themed items)
class ChristmasFactory(AbstractFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_toy(self, item):
        return ChristmasToy(item)

    def create_stuffed_animal(self, item):
        return Reindeer(item)

    def create_candy(self, item):
        return CandyCanes(item)


# HalloweenFactory (Concrete Class, extends AbstractFactory):
# Methods:
# (Implement create methods for Halloween-themed items)
class HalloweenFactory(AbstractFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_toy(self, item):
        return HalloweenToy(item)

    def create_stuffed_animal(self, item):
        return DancingSkeleton(item)

    def create_candy(self, item):
        return PumpkinCaramelToffee(item)


# EasterFactory (Concrete Class, extends AbstractFactory):
# Methods:
# (Implement create methods for Easter-themed items)
class EasterFactory(AbstractFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_toy(self, item):
        return EasterToy(item)

    def create_stuffed_animal(self, item):
        return EasterBunny(item)

    def create_candy(self, item):
        return CremeEggs(item)


class ItemFactory:
    factories = {
        "Christmas": ChristmasFactory(),
        "Halloween": HalloweenFactory(),
        "Easter": EasterFactory(),
    }

    @staticmethod
    def create_item(item: Item) -> Item:
        holiday = item.holiday_type
        item_type = item.item_type
        if holiday in ItemFactory.factories:
            factory = ItemFactory.factories[holiday]
            if item_type == "Toy":
                return factory.create_toy(item)
            elif item_type == "StuffedAnimal":
                return factory.create_stuffed_animal(item)
            elif item_type == "Candy":
                return factory.create_candy(item)
            else:
                raise ValueError(f"Invalid item type: {item_type}")
        else:
            raise ValueError(f"No factory registered for holiday: {holiday}")


# Order:
# Attributes:
# order_number: int
# item_type: ItemType
# product_id: str
# quantity: int
# item_name: str
# product_details: Dict[str, Any]
# factory: AbstractFactory
class Order:
    def __init__(self) -> None:
        self.item = None
        # self.order_number = 0
        # self.item_type = None
        # self.product_id = ""
        self.quantity = 0
        # self.item_name = ""
        # self.product_details = {}
        self.factory = None


# OrderProcessor:
# Attributes:
# factory_mapping: Dict[ItemType, AbstractFactory]
# Methods:
# process_order_row(row: Dict[str, Any]) -> Order
class OrderProcessor:
    def __init__(self) -> None:
        pass

    def process_order_row(self, row: dict) -> Order:
        order = Order()
        order.order_number = row["order_number"]
        order.item_type = row["item"]
        order.product_id = row["product_id"]
        order.quantity = row["quantity"]
        order.item_name = row["name"]
        order.holiday_type = row["holiday"]
        order.description = row["description"]
        # for k in (
        #     "order_number",
        #     "item",
        #     "product_id",
        #     "quantity",
        #     "name",
        #     "holiday",
        # ):
        #     row.pop(k)
        order.product_details = {}  # ["product_details"]
        try:
            order.product_details.setdefault("is_battery_operated", row["is_battery_operated"])
            order.product_details.setdefault("recommended_age", row["recommended_age"])
            order.product_details.setdefault("stuffing", row["stuffing"])
            order.product_details.setdefault("size", row["size"])
            order.product_details.setdefault("fabric", row["fabric"])
            order.product_details.setdefault("has_glow_in_dark", row["has_glow_in_dark"])
            order.product_details.setdefault("dimensions", row["dimensions"])
            order.product_details.setdefault("num_rooms", row["num_rooms"])
            order.product_details.setdefault("speed", row["speed"])
            order.product_details.setdefault("jump_height", row["jump_height"])
            order.product_details.setdefault("glows_in_dark", row["glows_in_dark"])
            order.product_details.setdefault("spider_type", row["spider_type"])
            order.product_details.setdefault("num_sound_effects", row["num_sound_effects"])
            order.product_details.setdefault("color", row["color"])
            order.product_details.setdefault("has_glow_in_dark_nose", row["has_glow_in_dark_nose"])
            order.product_details.setdefault("variety", row["variety"])
            order.product_details.setdefault("color_stripes", row["color_stripes"])
            order.product_details.setdefault("pack_size", row["pack_size"])
            order.product_details.setdefault("contains_nuts", row["contains_nuts"])
            order.product_details.setdefault("lactose_free", row["lactose_free"])
        except KeyError:
            pass
        return order


def read_excel_row_into_dict(filename):
    """
    # **Process Web Orders**

    # The store owner can go to their online storefront and download the orders received during the day in the form of an excel sheet.

    # Your code must prompt the user for the name of this file and use the pandas package to read them in and process the order.

    # **pandas** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of Python.
    """

    df = pd.read_excel(filename)
    # return df.to_dict("records")

    # Convert each row of the DataFrame to a dictionary and store in a list
    data_list = []
    for index, row in df.iterrows():
        row_dict = row.to_dict()
        data_list.append(row_dict)

    # Now, data_list contains a list of dictionaries, where each dictionary represents a row in the Excel file
    # print(data_list)
    return data_list


# Sequence Diagram:
# Main Sequence:
# User selects "Process Web Orders" from the menu.
# User provides the filename of the Excel sheet.
# OrderProcessor processes each row, creates an Order object, and sends it to the HolidayStore.
# HolidayStore checks if the item is in stock. If not, it uses the factory to order more.
# Order is added to the daily transaction report.
filename = "orders.xlsx"
orders = []
rows_list = read_excel_row_into_dict(filename)
for row_dict in rows_list:
    order_processor = OrderProcessor()
    order = order_processor.process_order_row(row_dict)
    orders.append(order)

holiday_store = HolidayStore()
for order in orders:
    holiday_store.process_web_orders(order)


# Check Inventory Sequence:
# User selects "Check Inventory" from the menu.
# HolidayStore displays a list of items with their information and stock status.
holiday_store.check_inventory()

# Exit Sequence:
# User selects "Exit" from the menu.
# HolidayStore generates the Daily Transaction Report and exits the program.
holiday_store.create_daily_transaction_report()
