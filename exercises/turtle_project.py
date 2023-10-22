"""TODO: Cozy home during a snowy day."""
__author__ = "730577037"
 
from turtle import Turtle, done
import random

def main() -> None:
    ertle: Turtle = Turtle()
    ertle.speed("fastest")
    draw_snowman(ertle, -250, -150, 20)
    draw_snowman(ertle, -250, -120, 15)
    draw_snowman(ertle, -250, -100, 10)
    draw_snowman(ertle, 200, -100, 20)
    draw_snowman(ertle, 200, -70, 15)
    draw_snowman(ertle, 200, -50, 10)
    draw_snowman(ertle, 0, -200, 20)
    draw_snowman(ertle, 0, -170, 15)
    draw_snowman(ertle, 0, -150, 10)
    draw_house(ertle, -175, 100, 240)
    draw_door(ertle, -80, -90, 50)
    draw_roof(ertle, -175, 100, 100)
    draw_window(ertle, -150, 10, 60)
    draw_window(ertle, -20, 10, 60)
    draw_window_fill(ertle, -120, -20, 60)
    draw_window_fill(ertle, 10, -20, 60)
    draw_chimney(ertle, 55, 120, 50)
    for snowflakes in range(30):
        draw_snowflake(ertle, 10)
    done()


def draw_snowman(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the circles of the snowman in 3 different locations."""
    a_turtle.up()
    a_turtle.goto(x, y - width)
    a_turtle.setheading(0)
    a_turtle.down()
    a_turtle.circle(width)
    a_turtle.up()


def draw_house(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the outline of the house."""
    a_turtle.color("black")
    a_turtle.up()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0)
    a_turtle.down()
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_door(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the door of the house."""
    a_turtle.color("brown")
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.setheading(0)
    a_turtle.down()
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.color("black")
    a_turtle.end_fill()


def draw_roof(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a roof on top of the house."""
    a_turtle.pencolor("white")
    a_turtle.fillcolor("black")
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.setheading(45)
    a_turtle.down()
    a_turtle.begin_fill()
    a_turtle.forward(width)
    a_turtle.right(45)
    a_turtle.forward(width)
    a_turtle.right(45)
    a_turtle.forward(width)
    a_turtle.end_fill()
    a_turtle.pencolor("black")
    

def draw_window(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw two windows for the house, but not the inside cross."""
    a_turtle.color("white")
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.setheading(0)
    a_turtle.down()
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.color("black")


def draw_window_fill(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw panes of windows for both windows."""
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.setheading(90)
    a_turtle.down()
    a_turtle.forward(0.5 * width)
    a_turtle.right(180)
    a_turtle.forward(width)
    a_turtle.right(180)
    a_turtle.forward(0.5 * width)
    a_turtle.right(90)
    a_turtle.forward(0.5 * width)
    a_turtle.right(180)
    a_turtle.forward(width)
    a_turtle.up()

def draw_chimney(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a chimney on the house."""
    a_turtle.color("brown")
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.setheading(90)
    a_turtle.begin_fill()
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(0.5 * width)
    a_turtle.left(90)
    a_turtle.forward(0.7 * width)
    a_turtle.left(45)
    a_turtle.forward(0.7 * width)
    a_turtle.left(135)
    a_turtle.forward(0.5 * width)
    a_turtle.end_fill()
    a_turtle.color("black")


def draw_snowflake(a_turtle: Turtle, width: float) -> None:
    """Draw 30 snowflakes at random positions around the screen."""
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.uniform(5, 20)
    a_turtle.up()
    a_turtle.goto(x, y)
    a_turtle.down()
    a_turtle.setheading(90)
    a_turtle.forward(width)
    a_turtle.right(180)
    a_turtle.forward(0.5 * width)
    a_turtle.right(90)
    a_turtle.forward(0.5 * width)
    a_turtle.right(180)
    a_turtle.forward(width)
    a_turtle.right(180)
    a_turtle.forward(0.5 * width)
    a_turtle.right(45)
    a_turtle.forward(0.5 * width)
    a_turtle.right(180)
    a_turtle.forward(width)
    a_turtle.right(180)
    a_turtle.forward(0.5 * width)
    a_turtle.right(90)
    a_turtle.forward(0.5 * width)
    a_turtle.right(180)
    a_turtle.forward(width)
    a_turtle.up()
    a_turtle.hideturtle()

if __name__ == "__main__":
    main()