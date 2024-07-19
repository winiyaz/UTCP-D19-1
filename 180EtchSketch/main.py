# 180 : Work for the etcher skectcher program

# 179 work

from turtle import Turtle, Screen

to = Turtle()  # Initialize Turtle Class
to.sc = Screen()  # Initialize Screen Class


# Turtle graphics initialize
def to_init():
	to.color("coral")  # Setting color
	to.shapesize(stretch_wid=3, stretch_len=3, outline=1)  # Setting size params
	to.sc.bgcolor("#020617")  # Set Bg Color

to_init()  # Initialize the turtle

# Screen Listener


# --- Exiting on click function
to.sc.exitonclick()