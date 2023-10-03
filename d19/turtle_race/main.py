from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
rainbow_colors = ["purple", "blue", "green", "yellow", "orange", "red"]


def main():
    """main"""
    turtles = []
    end_of_the_race = False
    color = screen.textinput("Make your bet", "Who will win the race ? Enter a color")
    for i, c in enumerate(rainbow_colors):
        new_turtle = Turtle("turtle")
        new_turtle.color(c)
        new_turtle.penup()
        new_turtle.goto((-200, -125 + 50 * i))
        turtles.append(new_turtle)
    while not end_of_the_race:
        for t in turtles:
            if t.xcor() > 230:
                end_of_the_race = True
                if t.pencolor() == color:
                    print(f"You win!. The {color} turtle is the winner")
                else:
                    print(f"You Lose. The {t.pencolor()} turtle is the winner")
            t.forward(random.randint(0, 10))


if __name__ == "__main__":
    main()
