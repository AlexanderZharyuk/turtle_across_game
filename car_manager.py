from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.shape('square')
        self.color(random.choice(COLORS))
        self.car_random_position()
        self.move_speed = STARTING_MOVE_DISTANCE

    def moving(self):
        self.forward(self.move_speed)

    def car_random_position(self):
        rand_y = random.randint(-250, 290)
        rand_x = random.randint(-240, 310)
        self.goto(rand_x, rand_y)

    def new_machine(self):
        rand_y = random.randint(-240, 290)
        self.goto(310, rand_y)

    def update_move_speed(self):
        self.move_speed += MOVE_INCREMENT