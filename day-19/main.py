from turtle import Turtle, Screen
from shape import InitTurtle
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["jimmy", "lola", "pri", "a", "b", "c"]
turtle_list = []
location_tuple = [(-230, -100), (-230, -60), (-230, -20), (-230, 20), (-230, 60), (-230, 100)]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

for position in range(len(names)):
    names[position] = Turtle(shape="turtle")
    turtle_list.append(names[position])

for i in range(len(turtle_list)):
    turtle_list[i].color(colors[i])

for turtle in range(len(turtle_list)):
    turtle_list[turtle].penup()
    turtle_list[turtle].goto(x=location_tuple[turtle][0], y=location_tuple[turtle][1])


if user_bet:
    is_race_on = True

while is_race_on:

    for bino in turtle_list:
        if bino.xcor() > 230:
            winning_color = bino.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")

            else:
                print(f"You've lost! the {winning_color} turtle is the winner")

        rand_instance = random.randint(0, 10)
        bino.forward(rand_instance)

screen.exitonclick()