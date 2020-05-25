
from rabbit import Rabbit

class Field:
    def __init__(self, array, objects_array, FIELD_LENGTH, FIELD_WIDTH):
        self.array = array
        self.objects_array = objects_array
        self.FIELD_LENGTH = FIELD_LENGTH
        self.FIELD_WIDTH = FIELD_WIDTH


    def new_rabbit(self, x, y):
        self.objects_array[x][y] = Rabbit(x,y, 8, self, 'r', 'c', 5)
        self.array[x][y] = 'r'

