from turtle import *

### write all new functions here ###

#Draw face
def draw_emoji(t): 
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("black", "yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    #Draw left eye
    t.penup()
    t.goto(-40, 40)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #Draw right eye
    t.penup()
    t.goto(40,40)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #Draw smile
    t.penup()
    t.goto(-40, 10)
    t.setheading(-60)
    t.pendown()
    t.width(5)
    t.circle(50, 120)

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """

    space = Screen()
    space.bgcolor("lightblue")

    t = Turtle()
    t.speed(5)

    draw_emoji(t)

    space.exitonclick()


if __name__ == '__main__':
    main()


