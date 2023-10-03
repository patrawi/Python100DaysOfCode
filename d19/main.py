"""Etch-A-Sketch App"""
from turtle import Turtle, Screen

cursor = Turtle()
s = Screen()
degree = 0


def forward():
    cursor.forward(50)


def backward():
    cursor.backward(50)


def counter_clockwise():
    current_heading = cursor.heading()
    cursor.setheading(current_heading - 10)


def clockwise():
    current_heading = cursor.heading()
    cursor.setheading(current_heading + 10)


def clear():
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()


def main():
    """main"""
    s.listen()
    s.onkey(fun=forward, key="w")
    s.onkey(fun=backward, key="s")
    s.onkey(fun=counter_clockwise, key="a")
    s.onkey(fun=clockwise, key="d")
    s.onkey(fun=clear, key="c")
    s.exitonclick()


if __name__ == "__main__":
    main()
