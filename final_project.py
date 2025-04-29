import pygame
import sys

pygame.init()

# screen stuff


def screen_setup():
    width = 900
    height = 600

    display = pygame.display.set_mode((900, 600))
    font = pygame.font.SysFont("Comfortaa", int(width / 20))
    bg = pygame.image.load("background2.jpg")
    bg = pygame.transform.scale(bg, (width, height))
    pygame.display.set_caption("Valeria Final Project Ping Pong")

    # clock = pygame.time.Clock()

    return height, width, display, bg


class Paddle:
    def __init__(self, x, y, width=10, height=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 2

    def move_up(self):
        pass

    def move_down(self):
        pass

    def speed_boost(self):
        pass

    def draw(self, display):
        pygame.draw.rect(display, "white", self.rect)


class Ball:
    def __init__(self, x, y, radius=10, speed=3):
        self.ball = pygame.Surface(x, y, radius=10)
        self.speed = 3

    def move(self):
        pass


"""
# OG paddles stuff
def paddles(height, width):
    you_1 = pygame.Rect(width - 800, int(height / 2 - 50), 10, 100)
    you_2 = pygame.Rect(width - 110, int(height / 2 - 50), 10, 100)

    return you_1, you_2
"""


def ball():
    pass


# game loop with attaching keys to paddles
def game_loop(you_1, you_2, height, bg, display):
    clock = pygame.time.Clock()

    while True:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            if you_2.rect.top > 0:
                you_2.rect.top -= 2
        if keys_pressed[pygame.K_DOWN]:
            if you_2.rect.bottom < height:
                you_2.rect.bottom += 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys_pressed[pygame.K_w]:
            if you_1.top > 0:
                you_1.top -= 2
        if keys_pressed[pygame.K_s]:
            if you_1.bottom < height:
                you_1.bottom += 2

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


def main():
    height, width, display, bg = (
        screen_setup()
    )  # used chat gpt to help debug main functions here
    you_1 = Paddle(width, height)
    you_2 = Paddle(width, height)
    game_loop(you_1, you_2, height, bg, display)


if __name__ == "__main__":
    main()
