import pgzrun
import random

WIDTH = 3440
HEIGHT = 1450
GRAVITY = 2000.0

class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = random.randint(-200, 200)
        self.vy = random.randint(-200, 200)
    
    def display(self):
        screen.draw.filled_circle((self.x, self.y), self.r, "blue")

balls = [
    Circle(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), random.randint(20, 50))
    for _ in range(5)
]

def draw():
    screen.clear()
    screen.fill("black")
    for ball in balls:
        ball.display()

def update(dt):
    for ball in balls:
        uy = ball.vy
        ball.vy += GRAVITY * dt
        ball.y += (uy + ball.vy) * 0.5 * dt
        ball.x += ball.vx * dt

        if ball.y > HEIGHT - ball.r:
            ball.vy = -ball.vy - 50
            ball.y = HEIGHT - ball.r
        elif ball.y < ball.r:
            ball.vy = -ball.vy - 50
            ball.y = ball.r

        if ball.x < ball.r:
            ball.vx = -ball.vx - 50
            ball.x = ball.r
        elif ball.x > WIDTH - ball.r:
            ball.vx = -ball.vx - 50
            ball.x = WIDTH - ball.r

def on_key_down(key):
    if key == keys.SPACE:
        for ball in balls:
            ball.vx += 1000
            ball.vy += 1000

pgzrun.go()
