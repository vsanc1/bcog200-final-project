import pygame
import sys
from random import randint

pygame.init()


# screen stuff
def screen_setup():
    width = 900
    height = 600

    display = pygame.display.set_mode((900, 600))
    font = pygame.font.SysFont("Comfortaa", 40)
    bg = pygame.image.load("background2.jpg")
    bg = pygame.transform.scale(bg, (width, height))
    pygame.display.set_caption("Valeria Final Project Ping Pong")

    # clock = pygame.time.Clock()

    return height, width, display, bg


# paddle object
class Paddle:
    def __init__(self, x, y, width=10, height=100):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 4

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def length_boost(self):
        pass

    def speed_bost(self):
        pass

    def draw(self, display):
        pygame.draw.rect(display, "white", self.rect)


# ball object
class Ball:
    def __init__(self, x, y, radius=10, speed_x=3, speed_y=3):
        self.ball = pygame.Rect(x, y, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius

    def move(self):
        self.ball.x += self.speed_x
        self.ball.y += self.speed_y

    def draw(self, display):
        pygame.draw.ellipse(display, "#66ccff", self.ball)


# game loop with paddle and ball logic
def game_loop(you_1, you_2, ball, width, height, bg, display):
    clock = pygame.time.Clock()

    you_1_score = 0
    you_2_score = 0
    font = pygame.font.SysFont("Comfortaa", 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            if you_2.rect.top > 0:
                you_2.move_up()
        if keys_pressed[pygame.K_DOWN]:
            if you_2.rect.bottom < height:
                you_2.move_down()

        if keys_pressed[pygame.K_w]:
            if you_1.rect.top > 0:
                you_1.move_up()
        if keys_pressed[pygame.K_s]:
            if you_1.rect.bottom < height:
                you_1.move_down()

        ball.move()

        # bounce off top and bottom
        if ball.ball.bottom >= height or ball.ball.top <= 0:
            ball.speed_y *= -1

        # reset if offscreen
        if ball.ball.left <= 0 or ball.ball.right >= width:
            ball.ball.center = (width / 2, height / 2)

        # ball hitting paddles - https://www.geeksforgeeks.org/adding-collisions-using-pygame-rect-colliderect-in-pygame/
        if ball.ball.colliderect(you_1.rect):
            ball.speed_x *= -1

        if ball.ball.colliderect(you_2.rect):
            ball.speed_x *= -1

        display.fill((0, 0, 0))
        if bg:
            display.blit(bg, (0, 0))

        you_1_score_text = f"Your score: {you_1_score}"
        you_2_score_text = f"Your 2nd score: {you_2_score}"

        you_1_score_render = font.render(str(you_1_score_text), True, "white")
        you_2_score_render = font.render(str(you_2_score_text), True, "white")

        display.blit(you_1_score_render, (150, 10))
        display.blit(you_2_score_render, (width - 350, 10))

        pygame.draw.rect(display, "white", you_1)
        pygame.draw.rect(display, "white", you_2)
        ball.draw(display)

        pygame.display.update()
        clock.tick(60)  # fps


def power_up(you_1, you_2):
    pass


def main():
    height, width, display, bg = (
        screen_setup()
    )  # used chat gpt to help me see how I was incorrectly passing arguments on April 18th 2025
    you_1 = Paddle(100, height / 2 - 50)
    you_2 = Paddle(width - 110, height / 2 - 50)
    ball = Ball(width / 2 - 10, height / 2 - 10)
    game_loop(you_1, you_2, ball, width, height, bg, display)


if __name__ == "__main__":
    main()
