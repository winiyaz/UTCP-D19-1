# 182: Understanding the turtle coordinate system
from turtle import Turtle, Screen
from rich import print as rprint

to = Turtle()  # Initialize Turtle Class
to.sc = Screen()  # Initialize Screen Class
to.sc.title("PantySmell")
to.speed("fastest")  # Speed of turtle
to.sc.bgcolor("#020617")
to.shapesize(stretch_wid=3, stretch_len=3, outline=1)  # Size
to.color("#c026d3")  # Set Color of turtle
to.sc.setup(width=800,height=600)  # Setting the screen size

# -- Actual Work --
user_bet = to.sc.textinput(title="Makbet", prompt="Colo?")  # Catching an input
rprint(f'Entered Input {user_bet}')

to.penup()
to.goto(x=-350, y=0)


# --- Exiting on click function
to.sc.exitonclick()
