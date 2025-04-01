import turtle as t
import pygame

pygame.init()

window_width = 800
window_height = 600
display = pygame.display.set_mode((window_width, window_height))
bg = pygame.image.load("background.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# window.title("Valeria Final Project Ping Pong")
# window.setup(800, 600)
# window.tracer(0)


YouScore = 0
You2Score = 0

paddle_1 = t.Turtle()
paddle_1.speed()
paddle_1.shape("circle")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto()

paddle_2 = t.Turtle()
paddle_2.speed()
paddle_2.shape("circle")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto()
