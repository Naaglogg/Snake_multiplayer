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
 
dis_width = 1920
dis_height = 1080
 
dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Змейка')
 
clock = pygame.time.Clock()





snake_block = 30
snake_speed = 15

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x1 = round(random.randrange(0, dis_width - snake_block) / 30.0) * 30.0
    y1 = round(random.randrange(0, dis_height - snake_block) / 30.0) * 30.0

    X_db = 0
    Y_db = 0
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change != snake_block and (X_db != x1 and Y_db != y1):
                    x1_change = -snake_block
                    X_db = x1
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change != -snake_block and (X_db != x1 and Y_db != y1):
                    x1_change = snake_block
                    X_db = x1
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change != snake_block and (X_db != x1 and Y_db != y1):
                    y1_change = -snake_block
                    Y_db = y1
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change != -snake_block and (X_db != x1 and Y_db != y1):
                    y1_change = snake_block
                    Y_db = y1                    
                    x1_change = 0
        if x1 > (dis_width - snake_block) or x1 < 0 or y1 > (dis_height - snake_block) or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True
 
        our_snake(snake_block, snake_List)

        pygame.display.update()

        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()