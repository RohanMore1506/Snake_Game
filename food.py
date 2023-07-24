import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)