from turtle import Turtle
import random

# piece of food on screen will be turtle object
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # food dimensions are 10 x 10
        self.color('blue')
        self.speed('fastest')
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)

    def refresh(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)
