from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
# keyword Argument
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
i = 0
for i in range(len(colors)):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-235, y=-100 + (i*50))
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
