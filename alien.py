from turtle import Turtle
import random

class Alien(Turtle):

    def __init__(self):
        super().__init__()
        self.alienlist = []

    def create_alien(self):
        alien = Turtle("alien")
        alien.penup()
        alien.color("green")
        alien.setheading(-90)
        random_x = random.randint(-270,270)
        random_y = random.randint(600,1100)
        alien.setx(random_x)
        alien.sety(random_y)
        self.alienlist.append(alien)


        


