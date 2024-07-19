# 182: Understanding the turtle coordinate system
import random as rp
from turtle import Turtle, Screen

from rich import print as rprint


sc = Screen()  # Initialize Screen Class
sc.title("PantySmell")

# to.shapesize(stretch_wid=3, stretch_len=3, outline=1)  # Size
# to.color("#c026d3")  # Set Color of turtle
to.sc.setup(width=800, height=600)  # Setting the screen size

# -- Actual Work --
user_bet = to.sc.textinput(title="Makbet", prompt="Colo?")  # Catching an input
rprint(f'Entered Input {user_bet}')

# to.penup()
# to.goto(x=-350, y=0)

neon_colors = [
	"#39FF14",  # Neon Green
	"#FF69B4",  # Neon Pink
	"#33CCFF",  # Neon Blue
	"#FFC67D",  # Neon Orange
	"#FF99FF",  # Neon Magenta
	"#33FF00",  # Neon Lime
	"#FF33CC",  # Neon Fuchsia
	"#66FF00",  # Neon Chartreuse
	"#CCFF00",  # Neon Yellow-Green
	"#FF0099",  # Neon Red-Pink
]

y_pos = [-70, -60, -40, 30, 20, 100]
to.color("#FF0099")

for tu_in in range(0, 6):
	to = Turtle(shape="turtle")
	to.penup()
	to.color(rp.choice(neon_colors))
	to.goto(x=-350, y=y_pos[tu_in])

to.speed("fastest")  # Speed of turtle
sc.bgcolor("#020617")

# --- Exiting on click function
to.sc.exitonclick()
