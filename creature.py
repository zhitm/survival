from random import randint
class Creature():
    def __init__(self, x, y, hunger_max, field, type, food_type, vision) :
        self.x = x
        self.y = y
        self.hunger = 0
        self.hunger_max = hunger_max
        self.field = field
        self.type = type
        self.food_type = food_type
        self.vision = vision
        self.turn_counter = 0

    def find_nearest(self, type):

        '''
        
        for i in range(self.field.FIELD_LENGTH):
            for j in range(self.field.FIELD_WIDTH):
                if self.field.array[i][j] == type:
                    dist = ((self.x - i) ** 2 + (self.y - j) ** 2) ** 0.5
                    if dist <= min_dist + 0.1 and dist != 0:
                        nearest = [i, j]
        '''
        nearest = None
        min_dist = self.vision + 0.1

        if self.x - self.vision < 0:
            left_x = 0
        else:
            left_x = self.x - self.vision
        if self.x + self.vision > self.field.FIELD_LENGTH:
            right_x = self.field.FIELD_LENGTH-1
        else:
            right_x = self.x + self.vision
        if self.y - self.vision < 0:
            down_y = 0
        else:
            down_y = self.y - self.vision
        if self.y + self.vision > self.field.FIELD_WIDTH:
            up_y = self.field.FIELD_WIDTH-1
        else:
            up_y = self.y + self.vision
        for i in range(right_x - left_x):
            for j in range(up_y - down_y ):
                if self.field.array[i + left_x][j + down_y] == type:
                    dist = ((self.x - i - left_x)**2+(self.y - j - down_y)**2  )**0.5
                    if dist <= min_dist + 0.1 and dist != 0:
                        min_dist = dist
                        nearest = [i+left_x, j+down_y]


        return nearest

    def random_move(self):
        vector = [randint(-2, 2), randint(-2, 2)]
        while self.x + vector[0] <= 0 or self.y + vector[1] <= 0 or self.x + vector[0] >= self.field.FIELD_LENGTH or self.y + vector[1] >= self.field.FIELD_WIDTH:
            # рандомим направление, пока не получим то, которое не выкинет зайца с поля
            vector = [randint(-2, 2), randint(-2, 2)]
        return vector


    def move(self, move):
        self.field.array[self.x][self.y] = 0
        self.field.objects_array[self.x][self.y] = 0
        self.x += move[0]
        self.y += move[1]
        self.field.array[self.x][self.y] = self.type
        self.field.objects_array[self.x][self.y] = self

    def go_to(self, coord):
        vector = [0, 0]
        if abs(coord[0]-self.x) <= 2 and abs(coord[1]-self.y) <= 2:  # если за один ход можно достичь - сразу туда прыгай
            vector = [coord[0] - self.x, coord[1] - self.y]
        elif self.x - coord[0] == self.y - coord[1]:  # если на это квадрат и за раз не дойти, то иди по диагонали и размашисто
            if self.x > coord[0]:
                vector[0] = -2
            else:
                vector[0] = 2
            if self.y > coord[1]:
                vector[1] = -2
            else:
                vector[1] = 2
        elif abs(coord[0] - self.x) >= 2 and abs(coord[1] - self.y) >= 2:  # надо идти примерно по диагонали прямоугольника, ищу его большую сторону
            if abs(coord[0] - self.x) > abs(coord[1] - self.x):
                if coord[0] - self.x > 0:
                    vector[0] = 2
                else:
                    vector[0] = -2
                if coord[1] - self.y > 0:
                    vector[1] = 1
                else:
                    vector[1] = -1
            else:
                if coord[0] - self.x > 0:
                    vector[0] = 1
                else:
                    vector[0] = -1
                if coord[1] - self.y > 0:
                    vector[1] = 2
                else:
                    vector[1] = -2
        else:
            if abs(coord[0] - self.x) <= 2:
                vector[0] = coord[0] - self.x
            if abs(coord[1] - self.y) <= 2:
                vector[1] = coord[1] - self.y
            if self.x != coord[0] and vector[0] == 0:
                if coord[0] > self.x:
                    vector[0] = 2
                else:
                    vector[0] = -2
            if self.y != coord[1] and vector[1] == 0:
                if coord[1] > self.y:
                    vector[1] = 2
                else:
                    vector[1] = -2

        while self.x + vector[0] <= 0:
            vector[0] += 2
        while self.x + vector[0] >= self.field.FIELD_LENGTH:
            vector[0] -= 2
        while self.y + vector[1] <= 0:
            vector[1] += 2
        while self.y + vector[1] >= self.field.FIELD_WIDTH:
            vector[1] -= 2
        return vector

    def go_away(self, coord):
        vector = [0, 0]
        if self.x > coord[0]:
            vector[0] = 2
        else:
            vector[0] = -2
        if self.y > coord[1]:
            vector[1] = 2
        else:
            vector[1] = -2
        while self.x + vector[0] <= 0:
            vector[0] += 1
        while self.x + vector[0] >= self.field.FIELD_LENGTH:
            vector[0] -= 1
        while self.y + vector[1] <= 0:
            vector[1] += 1
        while self.y + vector[1] >= self.field.FIELD_WIDTH:
            vector[1] -= 1


        return vector