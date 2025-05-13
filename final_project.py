import pygame
import sys

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
        self.powered_up = False
        self.powerup_start_time = 0

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def length_boost(self):  # this is a power up that increases paddle length
        self.rect.height += 80
        self.powered_up = True
        # self.powerup_start_time

    def de_power(self):  # reverts to normal state
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

    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)

    powerup_sfx = pygame.mixer.Sound("power_up.mp3")

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
        if ball.ball.left <= 0:
            you_2_score += 1
            ball.ball.center = (width / 2, height / 2)

        if ball.ball.right >= width:
            you_1_score += 1
            ball.ball.center = (width / 2, height / 2)

        # ball hitting paddles - https://www.geeksforgeeks.org/adding-collisions-using-pygame-rect-colliderect-in-pygame/
        if ball.ball.colliderect(you_1.rect):
            ball.speed_x *= -1

        if ball.ball.colliderect(you_2.rect):
            ball.speed_x *= -1

        display.fill((0, 0, 0))
        if bg:
            display.blit(bg, (0, 0))

        # scoreboard text
        you_1_score_text = f"Your score: {you_1_score}"
        you_2_score_text = f"Your 2nd score: {you_2_score}"

        # scoreboard show up onscreen
        you_1_score_render = font.render(str(you_1_score_text), True, "white")
        you_2_score_render = font.render(str(you_2_score_text), True, "white")

        display.blit(you_1_score_render, (150, 10))
        display.blit(you_2_score_render, (width - 350, 10))

        # showing paddle objects
        pygame.draw.rect(display, "white", you_1)
        pygame.draw.rect(display, "white", you_2)
        ball.draw(display)

        # power up activation after opponents score is 3 greater
        if you_2_score - you_1_score >= 3 and not you_1.powered_up:
            powerup_sfx.play()
            you_1.length_boost()

        if you_1_score - you_2_score >= 3 and not you_2.powered_up:
            powerup_sfx.play()
            you_2.length_boost()

        pygame.display.update()
        clock.tick(60)  # fps


# popup menu with intro / instructions / description
def intro_menu(display, width, height, bg):
    font = pygame.font.SysFont("Comfortaa", 30)
    title_font = pygame.font.SysFont("Comfortaa", 40, bold=True)

    intro = (
        "Hello! Welcome to my game.",
        "",
        "You will play pong with yourself or a friend.",
        "Use W S and the UP and DOWN arrows to control the paddles.",
        "When the opposing score is 3 greater, a power up will activate.",
        "",
        "Press SPACE to play.",
    )

    screen_width = 700
    screen_height = 300
    screen_x = (width - screen_width) // 2
    screen_y = (height - screen_height) // 2
    screen_rect = pygame.Rect(screen_x, screen_y, screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        display.fill((255, 255, 255))
        if bg:
            display.blit(bg, (0, 0))

        pygame.draw.rect(display, (255, 255, 255), screen_rect)
        pygame.draw.rect(display, (40, 40, 40), screen_rect, 3)

        for i, line in enumerate(intro):
            text_surface = font.render(line, True, "pink")
            text_rect = text_surface.get_rect(
                center=(screen_rect.centerx, screen_rect.top + 70 + i * 30)
            )
            display.blit(text_surface, text_rect)

            pygame.display.update()


def main():
    height, width, display, bg = (
        screen_setup()
    )  # used chat gpt to help me see how I was incorrectly passing arguments on April 18th 2025

    intro_menu(display, width, height, bg)

    you_1 = Paddle(100, height / 2 - 50)
    you_2 = Paddle(width - 110, height / 2 - 50)
    ball = Ball(width / 2 - 10, height / 2 - 10)

    game_loop(you_1, you_2, ball, width, height, bg, display)


if __name__ == "__main__":
    main()
