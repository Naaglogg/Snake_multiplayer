import random
import pygame
import time

pygame.init()
clock = pygame.time.Clock()


BLOCK = 30


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


display_w = pygame.display.Info().current_w
display_h = pygame.display.Info().current_h


screen = {
    'width_b' : display_w // BLOCK, # ширина экрана в клетках длины BLOCK
    'height_b' : display_h // BLOCK, # высота экрана в клетках длины BLOCK
}
screen['width_p'] = screen['width_b'] * BLOCK # ширина экрана в пикселях
screen['height_p'] = screen['height_b'] * BLOCK # высота экрана в пикселях
screen['barrier_w'] = (display_w - screen['width_p']) // 2 # барьеры по ширине с боков экранов в пикселях
screen['barrier_h'] = (display_h - screen['height_p']) // 2 # барьеры по высоте с боков экрана в пикселях
screen['width&border'] = screen['width_p'] + screen['barrier_w'] # ширина барьера и игрового поля для использования в .move()
screen['height&border'] = screen['height_p'] + screen['barrier_h'] # высота барьера и игрового поля для использования в .move()


snakes = []

def drawing(obj):
    """
    вывод обьекта на экран - змейки, яблока
    """
    for block in obj.blocks:
        pygame.draw.rect(dis, obj.color, (block.x, block.y, BLOCK, BLOCK))



def generate(size : int = 1):
    """
    генерация массива двух случайных координат x, y с учетом величины объекта в клетках BLOCK
    """
    x_coord = random.randint(0, screen['width_b'] - size) * BLOCK + screen['barrier_w']
    y_coord = random.randint(0, screen['height_b'] - size) * BLOCK + screen['barrier_h']
    return (x_coord, y_coord)

def opposite(a : str):
    opps = {
        "right" : "left",
        "left" : "right",
        "up" : "down",
        "down" : "up"
    }
    return opps[a]

class Coord(object):
    def __init__(self, x : int, y : int):
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
    def __init__(self, head : tuple, color : str = 'blue'):
        self.color = color
        self.head = Coord(head[0], head[1])
        self.blocks = [self.head]
        self.size = 1
        #prev = previous, предыдущий ход змейки
        self.prev = ''
        self.eat = 0

    def move(self, vector : str):
        """
        Move
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


        """
        Проход змеи из одной части рамки в другую при выходе за границы
        """
        if new_block.x < screen['barrier_w']:
            new_block.x = screen['width&border'] - BLOCK

        if new_block.x > screen['width&border'] - BLOCK:
            new_block.x = screen['barrier_w']

        if new_block.y < screen['barrier_h']:
            new_block.y = screen['height&border'] - BLOCK

        if new_block.y > screen['height&border'] - BLOCK:
            new_block.y = screen['barrier_h']


        blocks.insert(0, new_block)
        self.head = blocks[0]
        self.size += 1

        if not self.eat:
            blocks.pop()
            self.size -= 1
        else:
            self.eat -=1
            
    def collision(self, obj):
        head = self.head
        for block in obj.blocks:
            if (head.x == block.x) and (head.y == block.y):
                return True


class Apple(object):
    """
    apple
    Генерирует квадратное яблоко по заданной ширине, начиная от заданного левого верхнего угла
    
    Apple.blocks - {list} координатов всех клеток яблока {Coord}
    
    Apple.size - ширина стороны одного яблоках (в клетках) {int}
    """
    def __init__(self, block : list, size : int = 1, color : str = 'green'):
        self.blocks = [] 
        self.size = size
        self.color = color
        for y in range(self.size):
            for x in range(self.size):
                self.blocks.append(Coord(block[0] + BLOCK * x, block[1] + BLOCK * y))




"""
задание дисплея
"""
dis = pygame.display.set_mode((display_w, display_h))

apple = Apple(generate(2), 2)


''''''
vector = ''
''''''


while True:
    dis.fill(red)
    dis.fill(blue, (screen['barrier_w'], screen['barrier_h'], screen['width_b']*BLOCK, screen['height_b']*BLOCK))


    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_2:
                snakes.append(Snake(generate()))
            if event.key == pygame.K_w:
                vector = 'up'
            if event.key == pygame.K_a:
                vector = "left"
            if event.key == pygame.K_s:
                vector = 'down'
            if event.key == pygame.K_d:
                vector = 'right'
            
    drawing(apple)

    for snake_id in range(len(snakes)):
        snake = snakes[snake_id]

        drawing(snake)

        eat = False
        if snake.collision(apple):
            snake.eat += apple.size

            apple = Apple(generate(3), 3)
        if vector:
            snake.move(vector)



        
    pygame.display.update()
    clock.tick(15)


