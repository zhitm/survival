'''
Правила игры:
есть сколько-то охотников, сколько-то зайцев, сколько-то морковок в начале игры. Каждый ход на поле вырастает сколько-то морковки в случайных местах. Если зайчик не ел 5 ходов, то он исчезает.
Если два зайца оказались на соседних клетках, появляется еще один заец. Охотник ходит на одну и стреляет на одну или две клетки, заец бегает на 1 или 2 на его усмотрению
'''
from random import randint
from hunter import Hunter
from rabbit import Rabbit
from carrot import Carrot
from field import Field
from tkinter import *
import time
from creature import Creature
root = Tk()

root.geometry = '1000x1000'
root.title = 'SURVIVAL'
c = Canvas(width=1000, height=1000, bg='white')
c.pack()


class Main:

    def __init__(self):
        self.FIELD_LENGTH = 150
        self.FIELD_WIDTH = 150
        self.hunters = []
        self.rabbits = []
        self.carrots = []
        self.carrots_clone = []
        # self.game_list = [[0 for i in range(self.FIELD_LENGTH)] for i in range(self.FIELD_WIDTH)]
        self.num_hunters = 35
        self.num_rabbits = 1
        self.num_carrots = 50
        self.game_is_over = False
        arr = [[0 for i in range(self.FIELD_LENGTH)] for i in range(self.FIELD_WIDTH)]
        obj_arr = [[0 for i in range(self.FIELD_LENGTH)] for i in range(self.FIELD_WIDTH)]
        self.field = Field(arr, obj_arr, self.FIELD_LENGTH, self.FIELD_WIDTH)
        self.turn_counter = 0
        self.create_world()
        self.start()

    def create_world(self):
        for i in range(self.num_hunters):
            x = randint(2, self.FIELD_LENGTH - 2)
            y = randint(2, self.FIELD_WIDTH - 2)
            hunter = Hunter(x, y, 5, self.field, 'h', 'r', 5)
            self.field.objects_array[x][y] = hunter
            self.field.array[x][y] = 'h'
            self.hunters.append(hunter)

        for i in range(self.num_rabbits):
            x = randint(2, self.FIELD_LENGTH - 2)
            y = randint(2, self.FIELD_WIDTH - 2)
            rabbit = Rabbit(x, y, 5, self.field, 'r', 'c', 5)
            self.field.objects_array[x][y] = rabbit
            self.field.array[x][y] = 'r'
            self.rabbits.append(rabbit)

        for i in range(self.num_carrots):
            x = randint(2, self.FIELD_LENGTH - 2)
            y = randint(2, self.FIELD_WIDTH - 2)
            carrot = Carrot(x, y, self.field)
            self.field.array[x][y] = 'c'
            self.field.objects_array[x][y] = carrot
            self.carrots.append(carrot)
        self.carrots_clone = self.carrots
        self.update()

    def start(self):
        while not self.game_is_over:
            for rabbit in self.rabbits:
                rabbit.behavior()
            self.update_arrays()
            for hunter in self.hunters:
                hunter.behavior()
            self.turn_counter += 1
            if (self.turn_counter % 10) == 0: #каждые сколько-то ходов появляются заново морковки
                for carrot in self.carrots_clone:
                    if self.field.objects_array[carrot.x][carrot.y] == 0:
                        self.field.objects_array[carrot.x][carrot.y] = carrot
            time.sleep(0.5)
            self.update_arrays()
            self.game_state()
            self.update()

    '''
    Тут надо вызывать функцию поведения для каждого существа, а потом обновить карту
    '''

    def game_state(self):  # возвращает значение переменной game_is_over
        if len(self.rabbits) != 0:
            self.game_is_over = False
        else:
            self.game_is_over = True
            l = Label(c, text = 'ЗАЙЦЫ ВЫМЕРЛИ НА %x ХОДУ' %self.turn_counter, fg = 'red', font=("Helvetica", 25))
            l.pack()
    def update_arrays(self):
        self.hunters = []
        self.rabbits = []
        self.carrots = []
        for list in self.field.objects_array:
            for obj in list:
                if obj != 0:
                    if obj.type == 'h':
                        self.hunters.append(obj)
                        self.field.array[obj.x][obj.y] = 'h'
                    elif obj.type == 'r':
                        self.rabbits.append(obj)
                        self.field.array[obj.x][obj.y] = 'r'
                    elif obj.type == 'c':
                        self.carrots.append(obj)
                        self.field.array[obj.x][obj.y] = 'c'



    def update(self):  # рисует
        c.delete('all')

        for hunter in self.hunters:
            c.create_oval(hunter.x * 1000 / self.FIELD_LENGTH, hunter.y * 1000 / self.FIELD_WIDTH,
                          (hunter.x + 1) * 1000 / self.FIELD_LENGTH, (hunter.y + 1) * 1000 / self.FIELD_WIDTH,
                          fill='red')
        for rabbit in self.rabbits:
            c.create_oval(rabbit.x * 1000 / self.FIELD_LENGTH, rabbit.y * 1000 / self.FIELD_WIDTH,
                          (rabbit.x + 1) * 1000 / self.FIELD_LENGTH, (rabbit.y + 1) * 1000 / self.FIELD_WIDTH,
                          fill='blue')
        for carrot in self.carrots:
            c.create_oval(carrot.x * 1000 / self.FIELD_LENGTH, carrot.y * 1000 / self.FIELD_WIDTH,
                          (carrot.x + 1) * 1000 / self.FIELD_LENGTH, (carrot.y + 1) * 1000 / self.FIELD_WIDTH,
                          fill='orange')
        root.update()

if __name__ == '__main__':
    main = Main()
root.mainloop()
