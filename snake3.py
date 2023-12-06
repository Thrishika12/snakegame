import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (1, 0)

    def move(self):
        new_head = (
            (self.body[0][0] + self.direction[0] * CELL_SIZE) % WIDTH,
            (self.body[0][1] + self.direction[1] * CELL_SIZE) % HEIGHT
        )
        self.body.insert(0, new_head)
        if len(self.body) > 1:
            self.body.pop()

    def grow(self):
        self.body.append((-1, -1))

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return x, y

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

snake = Snake()
food = Food()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != (0, 1):
            snake.direction = (0, -1)
        elif keys[pygame.K_DOWN] and snake.direction != (0, -1):
            snake.direction = (0, 1)
        elif keys[pygame.K_LEFT] and snake.direction != (1, 0):
            snake.direction = (-1, 0)
        elif keys[pygame.K_RIGHT] and snake.direction != (-1, 0):
            snake.direction = (1, 0)

    snake.move()

    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.generate_position()

    screen.fill((0, 0, 0))
    snake.draw()
    food.draw()

    pygame.display.flip()

    clock.tick(10)
