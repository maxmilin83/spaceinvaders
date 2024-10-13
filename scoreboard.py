from turtle import Turtle,Screen

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 5
        self.hideturtle()
        self.penup()
        self.goto(-345,240)
        self.color("white")

    def update(self,score):
        self.score = score
        self.clear()
        self.write(f"Wave: {self.score}\nLives: {self.lives}",align='center',font=('Arial', 18, 'normal'))

    def win(self):
        self.clear()
        self.color("green")
        self.goto(0,0)
        self.write(f"YOU WIN",align='center',font=('Arial', 45, 'normal'))

    def lost(self):
        self.clear()
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER",align='center',font=('Arial', 45, 'normal'))
