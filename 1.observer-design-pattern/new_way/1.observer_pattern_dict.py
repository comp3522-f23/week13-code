def create_observer(name, update_func):
    return {"name": name, "update": update_func}


def iphone_update(message, name):
    print(f"iPhone user {name} got the news: {message}")


def android_update(message, name):
    print(f"Android user {name} got the news: {message}")


def attach_observer(observers, observer):
    observers.append(observer)


def detach_observer(observers, observer):
    # print(f"detaching {observer}")
    observers.remove(observer)


def notify_observers(observers, message):
    for observer in observers:
        observer["update"](message, observer["name"])


def main():
    observers = []

    jeff = create_observer("Jeff", iphone_update)
    eric = create_observer("Eric", android_update)

    attach_observer(observers, jeff)
    attach_observer(observers, eric)

    # Notify all observers
    notify_observers(observers, "It's snowing today!")

    # Detach one observer
    detach_observer(observers, eric)

    # Notify remaining observer
    notify_observers(observers, "Stocks are going up!")


if __name__ == "__main__":
    main()
