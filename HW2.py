# Your name: Clare Mathison
# Your student id: 7537 9681
# Your email: claremat@umich.edu
# List who or what you worked with on this homework: I used ChatGPT to help me figure out coordinates for the snowman
# If you used generative AI also include how you used it.
# Did your use of GenAI on this assignment align with your goals and guidelines in your Gen AI contract? If not, why? Yes! Asked for help, not direct answers. 

# import the turtle functions for use in this program
from turtle import *

### write all new functions here ###


# Draw snow globe
def draw_circle(turtle, fill_color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Draw snow globe base
def draw_rectangle(turtle, fill_color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(fill_color)
    turtle.begin_fill()
    for base in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_snow_globe(turtle):
    # Base
    draw_rectangle(turtle, "black", -120, -250, 240, 60)

    # Globe
    draw_circle(turtle, "darkblue", 0, -40, 180)

    # Snowman
    turtle.setheading(0)
    turtle.color("white")

    # Snowman body
    turtle.penup()
    turtle.goto(0, -140)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    # Snowman smile
    turtle.penup()
    turtle.goto(-10, 40)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.color("black")
    turtle.width(2)
    turtle.circle(12, 120)
    turtle.width(1)

    # Snowman eyes
    turtle.penup()
    turtle.goto(-10, 55)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(10, 55)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    # Buttons
    button_positions = [-50, -30, -10]
    for y in button_positions:
        turtle.penup()
        turtle.goto(0, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(4)
        turtle.end_fill()

    # Snowflakes 
    snowflakes = [
        (-120, 80), (-80, 120), (-40, 60), (0, 130), (40, 90), (80, 110), (120, 50), (-100, 0), (-60, -30), (-20, 50)
    ]

    turtle.color("white")
    for x, y in snowflakes:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(3)
        turtle.end_fill()

    # Scarf
    draw_rectangle(turtle, "red", -25, 12, 50, 8)
    draw_rectangle(turtle, "red", 15, -10, 8, 25)

    turtle.penup()
    turtle.goto(0, 200)

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_sglobe.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """

    space = Screen()
    space.bgcolor("lightpink")
    t = Turtle()
    t.speed(50)
    draw_snow_globe(t)
    space.exitonclick()

# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()


