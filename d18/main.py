from turtle import Turtle, Screen
import random
import colorgram

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "cyan",
    "magenta",
]

angles = [0, 90, 180, 270]


def generate_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color


def extract_color(image_name, number_of_colors):
    """extract color from image using colorgram"""
    return [e.rgb for e in colorgram.extract(image_name, number_of_colors)]


def main():
    """main function"""
    my_turtle.speed(0)
    my_turtle.pensize(5)
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.setheading(225)
    my_turtle.forward(300)
    my_turtle.setheading(0)

    colors = extract_color("dot_hirst.webp", 30)
    for i in range(100):
        my_turtle.dot(20, random.choice(colors))
        my_turtle.forward(50)
        if (i + 1) % 10 == 0:
            my_turtle.setheading(90)
            my_turtle.forward(50)
            my_turtle.setheading(180)
            my_turtle.forward(500)
            my_turtle.setheading(0)
    screen.exitonclick()


if __name__ == "__main__":
    main()
