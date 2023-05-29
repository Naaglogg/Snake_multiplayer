import pygame
import time
import random
 
pygame.init
 
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




BLOCK = 30

def opposite(a):
    opps = {
        "right" : "left",
        "left" : "right",
        "up" : "down",
        "down" : "up"
    }
    return opps[a]

class Coord(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def copy(self):
        return Coord(self.x, self.y)


class Snake(object):
    """
    snake
    генерирует первую клетку змеи по заданным координатам, потом постепенно увеличивает её

    Snake.color - цвет змейки {str}

    Snake.head - координаты головы змейки {Coord} - для сравнения с координатами яблока и с хитбоксами

    Snake.blocks - {list} координатов каждой клетки змейки {Coord}

    Snake.size - длина змейки {int}

    Snake.prev - направление последнего движения {str} - для ограничения движений и постоянного движения в заданную сторону

    Snake.move(vector, eat) - движение по заданному направлению vector {str} с возможностью продлить змейку при eat = True {bool}
    """
    def __init__(self, head, color = black):
        self.color = color
        self.head = Coord(head[0], head[1])
        self.blocks = [self.head]
        self.size = 1
        #prev = previous, предыдущий
        self.prev = 'down'
        self.eat = 0

    def move(self, vector, collide = False):
        """
        Move
        ИЗМЕНИТЬ ОППОСИТ
        """
        blocks = self.blocks
        new_block = self.head.copy()
        if opposite(vector) != self.prev:
            self.prev = vector
            
        if self.prev == 'right':
            new_block.x += BLOCK

        if self.prev == 'left':
            new_block.x -= BLOCK

        if self.prev == 'up':
            new_block.y -= BLOCK

        if self.prev == 'down':
            new_block.y += BLOCK

        blocks.insert(0, new_block)
        self.head = blocks[0]
        self.size += 1

        if not self.eat:
            blocks.pop()
            self.size -= 1
        else:
            self.eat -=1


class Apple(object):
    """
    apple
    Генерирует квадратное яблоко по заданной ширине, начиная от заданного левого нижнего угла
    
    Apple.blocks - {list} координатов всех клеток яблока {Coord}
    
    Apple.size - ширина стороны одного яблоках (в клетках) {int}
    """
    def __init__(self, block, size=1):
        self.blocks = [] 
        self.size = size
        for y in range(self.size):
            for x in range(self.size):
                self.blocks.append(Coord(block[0] + BLOCK * y, block[1] - BLOCK * x))
        







apl1 = Apple((30, 90))
'''
blocks = apl1.blocks
for i in blocks:
    print(i.x, i.y)
'''

snak1 = Snake((0, 0))




def want_to_move(vector, eat = False):
    """
    nice
    """
    snak1.move(vector, eat)
    for i in range(snak1.size):
        block = snak1.blocks[i]
        print('block n ', i + 1, 'coords = ', block.x, block.y)
"""

#want_to_move('right', False)


v - vector, направление движения
e - eat, параметр поедания

v, e = input().split()
e = bool(int(e))
while v != '0':
    want_to_move(v, e)
    v, e = input().split()
    e = bool(int(e))
    print('Создатель, за что?')
    print('Создатель, убейте меня!')
"""




def element_print(blocks, BLOCK, color=red):
    for block in blocks: #
        pygame.draw.rect(dis, color, [block.x, block.y, BLOCK, BLOCK])

def gameLoop():
    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    snake1 = Snake((round(random.randrange(0, dis_width - BLOCK) / 30.0) * 30.0, round(random.randrange(0, dis_height - BLOCK) / 30.0) * 30.0), green)
    snake2 = Snake((round(random.randrange(0, dis_width - BLOCK) / 30.0) * 30.0, round(random.randrange(0, dis_height - BLOCK) / 30.0) * 30.0))
    while not game_over:

        dis.fill(blue)
        element_print(snake1.blocks, BLOCK, snake1.color)
        vector1 = snake1.prev

        element_print(snake2.blocks, BLOCK, snake2.color)
        vector2 = snake2.prev
        eat=False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_w:
                    vector1 = 'up'
                elif event.key == pygame.K_a:
                    vector1 = 'left'
                elif event.key == pygame.K_s:
                    vector1 = 'down'
                elif event.key == pygame.K_d:
                    vector1 = 'right'
                if event.key == pygame.K_UP:
                    vector2 = 'up'
                elif event.key == pygame.K_LEFT:
                    vector2 = 'left'
                elif event.key == pygame.K_DOWN:
                    vector2 = 'down'
                elif event.key == pygame.K_RIGHT:
                    vector2 = 'right'
        snake1.move(vector1)
        snake2.move(vector2)

        pygame.display.update()

        clock.tick(15)

gameLoop()