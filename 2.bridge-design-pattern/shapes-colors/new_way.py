import abc


# Color implementation functions
def create_red():
    def color():
        return "Red"

    return color


def create_blue():
    def color():
        return "Blue"

    return color


# Abstraction functions
def create_shape(color_func):
    def draw_shape():
        print(f"I am a Shape with color {color_func()}")

    return draw_shape


def create_square(color_func):
    def draw_square():
        print(f"I am a Square with color {color_func()}")

    return draw_square


def create_circle(color_func):
    def draw_circle():
        print(f"I am a Circle with color {color_func()}")

    return draw_circle


def main():
    print("---- COMBO 1: Red Square ----")
    red_square = create_square(create_red())
    red_square()

    print("\n---- COMBO 2: Blue Circle ----")
    blue_circle = create_circle(create_blue())
    blue_circle()

    print("\n---- COMBO 3: Red Circle ----")
    red_circle = create_circle(create_red())
    red_circle()


if __name__ == "__main__":
    main()
