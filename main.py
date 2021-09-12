import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SneekOS')

clock = pygame.time.Clock()

snakeSize = 10
snakeSpeed = 15

fontStyle = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("timesnewroman", 25)


def scoreboard(score):
    value = scoreFont.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])


def playersnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    display.blit(mesg, [display_width / 4, display_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snakeSize) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snakeSize) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            scoreboard(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeSize
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeSize
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeSize
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeSize
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snakeSize, snakeSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        playersnake(snakeSize, snake_List)
        scoreboard(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snakeSize) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snakeSize) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()
