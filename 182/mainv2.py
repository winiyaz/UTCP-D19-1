# main.py giving trouble so rewriting the code here

import random as rp
from turtle import Screen, Turtle
from rich import print as rprint

sc = Screen()
sc.setup(width=800, height=600)  # Window Size
sc.title("PantySmell")  # Title
sc.bgcolor("#020617")  # BG Color

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

# getting user input
user_bet = sc.textinput(title="Makbet", prompt="Colo?")  # Catching an input
rprint(f'Entered Input {user_bet}')

y_pos = [-90, -40, -10, 90, 60, 30]

for tu_in in range(0, 6):
	to = Turtle(shape="turtle")
	to.shapesize(stretch_wid=3, stretch_len=3, outline=1)
	to.penup()
	to.color(rp.choice(neon_colors))
	to.goto(x=-350, y=y_pos[tu_in])


# Exiting on click
sc.exitonclick()
