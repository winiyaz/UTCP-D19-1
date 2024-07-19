# main.py giving trouble so rewriting the code here

import random as rp
import turtle
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

y_pos = [-150, -30, -15, 100, 160, 260]

is_race_on = False  # For While Loop

all_turtles = []

for tu_in in range(0, 6):
	ne_tu = Turtle(shape="turtle")
	ne_tu.shapesize(stretch_wid=3, stretch_len=3, outline=1)
	ne_tu.penup()
	ne_tu.color(rp.choice(neon_colors))
	ne_tu.goto(x=-350, y=y_pos[tu_in])
	all_turtles.append(ne_tu)

if user_bet:
	is_race_on = True

while is_race_on:

	for tu in all_turtles:
		if tu.xcor() > 350:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				rprint(f'Won {winning_color}')
			else:
				rprint(f'lost {winning_color}')

		rand_distance = rp.randint(0, 10)
		tu.forward(rand_distance)

# Exiting on click
sc.exitonclick()
