from turtle import Turtle, Screen
import random
SHAPES = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
VIBRANT_COLORS = ["red", "orange", "yellow", "lime", "cyan", "blue", "purple", "magenta", "gold", "chartreuse"]
class Food(Turtle):
     def __init__(self):
        super().__init__()
        self.random_shape()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.random_color()
        self.speed("fastest")
        self.refresh()


     def refresh(self):
        self.random_shape()
        self.color(random.choice(VIBRANT_COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

     def random_shape(self):
        self.shape(random.choice(SHAPES))

     def random_color(self):
        self.color(random.choice(VIBRANT_COLORS))