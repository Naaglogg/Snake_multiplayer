SNAKE_STEP = 30
print("Введите границы игры x,y в пиксели")
barrier=[int(i)-30 for i in input().split()]
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
    def __init__(self, color, head):
        self.color = color
        self.head = Coord(head[0], head[1])
        self.blocks = [self.head]
        self.size = 1
        #prev = previous, предыдущий
        self.prev = ''

    def move(self, vector, eat = False):
        """
        Move

        """
        
        
        if opposite(vector) != self.prev:
            blocks = self.blocks
            new_block = self.head.copy()

            if vector == 'right':
                new_block.x += SNAKE_STEP

            if vector == 'left':
                new_block.x -= SNAKE_STEP

            if vector == 'up':
                new_block.y -= SNAKE_STEP

            if vector == 'down':
                new_block.y += SNAKE_STEP

            self.prev = vector

            blocks.insert(0, new_block)
            self.head = blocks[0]
            self.size += 1

            if not eat:
                blocks.pop()
                self.size -= 1
            

class Bomb(object):
    """
    bomb
    Генерирует квадратную бомбу по заданной ширине, начиная от заданного левого нижнего угла
    
    Bomb.blocks - {list} координатов всех клеток бомб {Coord}
    
    Bomb.size - ширина стороны одной бомбы (в клетках) {int}
    """
    def __init__(self, block, size=1):
        self.blocks = [] 
        self.size = size
        for y in range(self.size):
            for x in range(self.size):
                self.blocks.append(Coord(block[0] + SNAKE_STEP * y, block[1] - SNAKE_STEP * x))
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
                self.blocks.append(Coord(block[0] + SNAKE_STEP * y, block[1] - SNAKE_STEP * x))
        







apl1 = Apple((30, 90))
'''
blocks = apl1.blocks
for i in blocks:
    print(i.x, i.y)
'''

snak1 = Snake('red', (0, 0))

def screenmove(barrier):
    """
    barrier - это пиксели экрана
    
    """
    if snak1.head.x < 0:
        snak1.head.x = (barrier[0] // SNAKE_STEP) * SNAKE_STEP
    elif snak1.head.x > ( barrier[0] // SNAKE_STEP) * SNAKE_STEP:
        snak1.head.x = 0
    if snak1.head.y < 0:
        snak1.head.y = (barrier[1] // SNAKE_STEP) * SNAKE_STEP
    elif snak1.head.y > (barrier[1] // SNAKE_STEP) * SNAKE_STEP:
        snak1.head.y = 0
        
    
    
        


def want_to_move(vector, eat = False):
    """
    nice
    """
    snak1.move(vector, eat)
    global barrier
    screenmove(barrier)
    for i in range(snak1.size):
        block = snak1.blocks[i]
        print('block n ', i + 1, 'coords = ', block.x, block.y)

#want_to_move('right', False)

"""
v - vector, направление движения
e - eat, параметр поедания
"""
v, e = input().split()
e = bool(int(e))
while v != '0':
    want_to_move(v, e)
    v, e = input().split()
    e = bool(int(e))