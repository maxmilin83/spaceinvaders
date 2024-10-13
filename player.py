from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("spaceship")
        self.color("gray")
        self.setheading(90)
        self.penup()
        self.goto(0,-250)
        self.shapesize(2)
        self.bulletlist = []

    def shoot(self):
        bullet = Turtle(shape="square")
        bullet.shapesize(stretch_len=0.35,stretch_wid=1.4)
        bullet.penup()
        bullet.color("white")
        bullet.goto( (self.xcor(),self.ycor() + 55))
        self.bulletlist.append(bullet)
    
    def left(self):
        current_x = self.xcor()
        if current_x > -350:
         self.setx(current_x - 45)

    def right(self):
        current_x = self.xcor()
        if current_x < 350:
            self.setx(current_x + 45)

    

        
    

