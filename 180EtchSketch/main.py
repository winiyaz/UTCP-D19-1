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


# Work will be done here

def mo_fo():
	"""Moving forward Function"""
	to.color("#FF0080")
	to.setheading(0)
	to.forward(50)

def mo_ba():
	"""Moving backward"""
	to.color("#FFFF80")
	to.setheading(180)  # This turns the head letting it go backward
	to.forward(50)

def mo_up():
	"""Moing Up"""
	to.setheading(90)
	to.color("#FFAA80")
	to.forward(50)

def mo_do():
	"""Moing Up"""
	to.setheading(270)
	to.color("#FF5580")
	to.forward(50)


to.sc.listen()  # Initialize the screen listener function
to.sc.onkey(mo_fo, "w")
to.sc.onkey(mo_ba, "e")
to.sc.onkey(mo_up, "r")
to.sc.onkey(mo_do, "t")

# --- Exiting on click function
to.sc.exitonclick()
