from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from managecars import ManageCars
import time

screen = Screen()
screen.setup(width=600, height=600)
scoreboard = ScoreBoard()
screen.tracer(0)
player = Player()
car_manager = ManageCars()
screen.listen()
screen.onkey(player.go_up, "Up")
game_speed = car_manager.car_speed
game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()
    # Detect when turtle reaches the other side.
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.add_score()
        game_speed *= 0.5

    # Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
