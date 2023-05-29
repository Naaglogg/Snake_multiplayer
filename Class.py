BLOCK = 30

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
    def __init__(self, head : tuple, color : str = 'black'):
        self.color = color
        self.head = Coord(head[0], head[1])
        self.blocks = [self.head]
        self.size = 1
        #prev = previous, предыдущий
        self.prev = ''
        self.eat = 0

    def move(self, vector : str, collide : bool = False):
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
    Генерирует квадратное яблоко по заданной ширине, начиная от заданного левого нижнего угла
    
    Apple.blocks - {list} координатов всех клеток яблока {Coord}
    
    Apple.size - ширина стороны одного яблоках (в клетках) {int}
    """
    def __init__(self, block : list, size : int = 1, color : str = 'red'):
        self.blocks = [] 
        self.size = size
        self.color = color
        for y in range(self.size):
            for x in range(self.size):
                self.blocks.append(Coord(block[0] + BLOCK * x, block[1] - BLOCK * y))





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
    print('Создатель, за что?')
    print('Создатель, убейте меня!')