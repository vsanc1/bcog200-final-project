import pygame
import sys

pygame.init()

# screen stuff
width, height = 900, 600


display = pygame.display.set_mode((900, 600))
font = pygame.font.SysFont("Comfortaa", int(width / 20))
bg = pygame.image.load("background2.jpg")
bg = pygame.transform.scale(bg, (width, height))
pygame.display.set_caption("Valeria Final Project Ping Pong")


clock = pygame.time.Clock()


# paddles stuff
you_1 = pygame.Rect(width - 800, int(height / 2 - 50), 10, 100)
you_2 = pygame.Rect(width - 110, int(height / 2 - 50), 10, 100)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0, 0, 0))
    if bg:
        display.blit(bg, (0, 0))

    pygame.draw.rect(display, "white", you_1)
    pygame.draw.rect(display, "white", you_2)

    pygame.display.update()
    clock.tick(60)  # fps
