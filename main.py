from turtle import Turtle,Screen
from player import Player
from alien import Alien
from scoreboard import Score
import time

ALIEN_SPEED = 4
CURRENT_WAVE = -1


screen = Screen()
screen.setup(width=800,height=600)
screen.title("Spaceship Invaders")
screen.bgpic("images/background.gif")


spaceship_shape = ((0, 20), (10, 10), (18, 10), (22, 5), (22, 0), (18, -5), (10, -10), (6, -15), (-6, -15), (-10, -10), (-18, -5), (-22, 0), (-22, 5), (-18, 10), (-10, 10))
alien_shape = ((0, 35), (-15, 25), (-10, 15), (-25, 0), (-10, -10), (-5, -35),
               (5, -35), (10, -10), (25, 0), (10, 15), (15, 25))

screen.register_shape("spaceship",spaceship_shape)
screen.register_shape("alien",alien_shape)

# intro_text = Turtle()
# intro_text.goto(0,0)
# intro_text.hideturtle()
# intro_text.color("Green")
# intro_text.write("Press Any Key To Play", align="center", font=("Arial", 42, "normal"))

screen.listen()
screen.tracer(0)

player = Player()
alien = Alien()
scoreboard = Score()



screen.onkey(player.left,"Left")
screen.onkey(player.right,"Right")
screen.onkey(player.shoot,"Up")



game = True
alienWaves = [6,8,10,12,14]  #List of alien amounts in each wave.

while game:
    time.sleep(0.1)
    screen.update()
    
    x = alienWaves[CURRENT_WAVE]

    current_round = True

    while current_round:
        time.sleep(0.1)
        screen.update()
        scoreboard.update(CURRENT_WAVE)

        if scoreboard.lives <= 0:
            scoreboard.lost()
            game = False
            current_round = False

        if not alien.alienlist:  #check if aliens exist
            if CURRENT_WAVE == (len(alienWaves)-1):
                scoreboard.win()
                current_round = False
                game = False
            
            CURRENT_WAVE+=1
            ALIEN_SPEED+=1
            try:
                x = alienWaves[CURRENT_WAVE]
            except IndexError:
                pass

            while x > 0:  #create aliens
                alien.create_alien()
                x = x-1
        
        for al in alien.alienlist: #move aliens and check if lost lifes
            if al.ycor() < -280 and scoreboard.lives > 0:
                al.hideturtle()
                alien.alienlist.remove(al)
                scoreboard.lives -= 1
            
                    
            currenty = al.ycor()
            al.sety(currenty - ALIEN_SPEED)
            
        for bullet in player.bulletlist: #shoot bullets
            current_y = bullet.ycor()
            bullet.sety(current_y + 20)
        
        for bullet in player.bulletlist: #check if bullet is hitting aliens
            for al in alien.alienlist:

                if bullet.distance(al) < 30 and al.ycor() < 300:
                    al.hideturtle()
                    alien.alienlist.remove(al)


    
screen.exitonclick() 


