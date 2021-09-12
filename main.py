import pygame
import random
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

snake_block = 10

imageS = pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\Snakeathon\Snek.jpg')
imageN = pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\Snakeathon\Nice.jpg')
imageA = pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\Snakeathon\Apple.jpg')
imageK = pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\Snakeathon\King.jpg')
imageE = pygame.image.load(r'C:\Users\DELL\OneDrive\Desktop\Snakeathon\Elephant.jpg')

imgArray = [imageS, imageN, imageE, imageE, imageK]

dis_width = 500
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by SneekOS')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    if x1 = foodx and y1 = foody

    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()

# display code ends here
