from turtle import Turtle
import random

color_list = [
    "Red",
    "Green",
    "Blue",
    "Yellow",
    "Cyan",
    "Magenta",
    "Orange",
    "Purple",
    "Pink",
    "Teal"
]
STARTING_MOVE_DISTANCE = 5


class ManageCars:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1

    def create_car(self):
        random_chance = 1
        if random_chance == random.randint(1, 10):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(color_list))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


