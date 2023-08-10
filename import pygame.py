import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


def colisao(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def is_collision_with_wall(pos):
    return pos[0] < 0 or pos[0] >= 600 or pos[1] < 0 or pos[1] >= 600

def is_collision_with_self(snake):
    return snake[0] in snake[1:]

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

direction_snake = LEFT

clock = pygame.time.Clock()

game_over = False

while not game_over:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction_snake = UP
            if event.key == K_DOWN:
                direction_snake = DOWN
            if event.key == K_RIGHT:
                direction_snake = RIGHT
            if event.key == K_LEFT:
                direction_snake = LEFT

    if colisao(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    new_head = None
    if direction_snake == UP:
        new_head = (snake[0][0], snake[0][1] - 10)
    if direction_snake == DOWN:
        new_head = (snake[0][0], snake[0][1] + 10)
    if direction_snake == RIGHT:
        new_head = (snake[0][0] + 10, snake[0][1])
    if direction_snake == LEFT:
        new_head = (snake[0][0] - 10, snake[0][1])

    if is_collision_with_wall(new_head) or is_collision_with_self(snake):
        game_over = True

    snake.insert(0, new_head)
    if snake[0] == apple_pos:
        apple_pos = on_grid_random()
    else:
        snake.pop()

    tela.fill((0, 0, 0))
    tela.blit(apple, apple_pos)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()


font = pygame.font.Font(None, 36)
text = font.render("Game Over", True, (255, 255, 255))
text_rect = text.get_rect(center=(300, 300))
tela.blit(text, text_rect)
pygame.display.update()


waiting_for_key = True
while waiting_for_key:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            waiting_for_key = False
            pygame.quit()

pygame.quit()
