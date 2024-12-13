import pgzrun
import random
WIDTH = 3440
HEIGHT = 1450
GRAVITY = 2000.0
class Circle():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 200
        self.vy = 0
    def display(self):
        screen.draw.filled_circle((self.x,self.y),self.r, "blue")


ball = Circle(100,100,30)
def draw():
    screen.clear()
    screen.fill("black")
    ball.display()
    
def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    ball.x += ball.vx*dt
    if ball.y>HEIGHT-30:
        ball.vy = ball.vy*-1 - 50
    elif ball.y<0:
        ball.vy = ball.vy*-1 - 50
    if ball.x<0:
        ball.vx = ball.vx*-1 - 50
    elif ball.x>WIDTH-30:
        ball.vx = ball.vx*-1 - 50
def on_key_down(key):
    if key == keys.SPACE:
        ball.vx = ball.vx + 1000
        ball.vy = ball.vy + 1000
    
pgzrun.go()


    
