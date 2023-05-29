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
snake_speed = 0
 
font_style = pygame.font.SysFont("Times New Roman", 35)
score_font = pygame.font.SysFont("Times New Roman", 35)
menu_font = pygame.font.SysFont("Times New Roman", 35)

easy = 0
normal = 0
hard = 0
 
def Your_score(score):
    value = score_font.render("Очки: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 2])
 
 
def gameLoop():
    MENU = True
    game_over = False
    game_close = False
    global snake_speed
    global easy
    global normal
    global hard

    x1 = round(random.randrange(0, dis_width - snake_block) / 30.0) * 30.0
    y1 = round(random.randrange(0, dis_height - snake_block) / 30.0) * 30.0

    X_db = 0
    Y_db = 0
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 30.0) * 30.0
    foody = round(random.randrange(0, dis_height - snake_block) / 30.0) * 30.0
 
    while not game_over:
        while MENU == True:
            dis.fill(blue)
            a = menu_font.render(str('Выберите сложность:'), True, green)
            b = menu_font.render(str('1 - easy'), True, green)
            c = menu_font.render(str('2 - normal'), True, green)
            d = menu_font.render(str('3 - hard'), True, green)
            dis.blit(a, (dis_width / 3, dis_height / 3))
            dis.blit(b, (dis_width / 3, dis_height / 3 + 40))
            dis.blit(c, (dis_width / 3, dis_height / 3 + 80))
            dis.blit(d, (dis_width / 3, dis_height / 3 + 120))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        snake_speed = 9
                        easy = 1
                        MENU = False
                    if event.key == pygame.K_2:
                        snake_speed = 12
                        normal = 1
                        MENU = False
                    if event.key == pygame.K_3:
                        snake_speed = 20
                        hard = 1
                        MENU = False

 
        while game_close == True:
            dis.fill(blue)
            message("Поражение! Нажмите Esc-выйти или Enter-продолжить", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update() 
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 30.0) * 30.0
            foody = round(random.randrange(0, dis_height - snake_block) / 30.0) * 30.0
            Length_of_snake += 1
            if (Length_of_snake - 1) % 5 == 0:
                if easy == 1:
                    snake_speed += 1.5
                if normal == 1:
                    snake_speed += 2
                if hard == 1:
                    snake_speed += 2.5
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()
