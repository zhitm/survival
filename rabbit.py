from creature import Creature

class Rabbit(Creature):

    def __init__(self, x, y, hunger_max, field, type, food_type, vision):
        self.x = x
        self.y = y
        self.field = field
        self.hunger = 0
        self.hunger_max = hunger_max
        self.vision = vision
        self.type = type
        self.turn_counter = 0
        self.food_type = food_type
        self.replication_age = 6


    def behavior(self):
        self.turn_counter += 1
        hunter_coord = super().find_nearest('h')
        if hunter_coord != None:
            self.hunger += 1
            move = super().go_away(hunter_coord)
        else:
            carrot_coord = super().find_nearest('c')
            if carrot_coord != None:
                if abs(carrot_coord[0] - self.x) <= 2 and abs(carrot_coord[1] - self.y) <= 2:
                    self.hunger = 0
                else:
                    self.hunger += 1
                move = super().go_to(carrot_coord)
            elif self.turn_counter >= self.replication_age:
                rabbit_coord = super().find_nearest('r')
                if rabbit_coord != None and self.turn_counter >=self.replication_age and self.field.objects_array[rabbit_coord[0]][rabbit_coord[1]].turn_counter >=self.replication_age:
                    move = super().go_to(rabbit_coord)
                    if abs(rabbit_coord[0] - self.x) <= 2 and abs(rabbit_coord[1] - self.y) <= 2 :
                        self.child()
                else:
                    self.hunger += 1
                    move = super().random_move()
            else:
                self.hunger += 1
                move = super().random_move()
        if self.hunger == self.hunger_max:
            self.die()
        else:
            super().move(move)

    def child(self):
        if self.x + 2 < self.field.FIELD_LENGTH:
            if self.field.array[self.x+2][self.y] == 0:
                self.field.new_rabbit(self.x+2, self.y)
        if self.x - 2 > 0:
            if self.field.array[self.x-2][self.y] == 0:
                self.field.new_rabbit(self.x-2, self.y)
        if self.y - 2 > 0:
            if self.field.array[self.x][self.y-2] == 0:
                self.field.new_rabbit(self.x, self.y - 2)
        if self.y + 2 < self.field.FIELD_WIDTH:
            if self.field.array[self.x][self.y+2] == 0:
                self.field.new_rabbit(self.x, self.y+2)
    def die(self):
        self.field.objects_array[self.x][self.y] = 0
        self.field.array[self.x][self.y] = 0