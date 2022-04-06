import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, 'Up')

cars = []
for _ in range(10):
    new_car = CarManager()
    cars.append(new_car)

game_is_on = True
while game_is_on:
    for car in cars:
        if car.xcor() < -300:
            car.new_machine()
        car.moving()
        # check collision car with player
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        player.level_complete()

        for car in cars:
            car.update_move_speed()

    time.sleep(0.1)
    screen.update()
