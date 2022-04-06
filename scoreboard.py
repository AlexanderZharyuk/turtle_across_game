from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.write_scoreboard()

    def write_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.pencolor('black')
        self.write(f'LEVEL: {self.level}',align='left', font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f'LEVEL: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER!', align='center', font=FONT)
        time.sleep(3)
