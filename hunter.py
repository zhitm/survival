from creature import Creature
class Hunter(Creature):
    def __init__(self, x, y, hunger_max, field, type, food_type, vision):
        self.x = x
        self.y = y
        self.hunger = 0
        self.hunger_max = hunger_max
        self.field = field
        self.type = type
        self.food_type = food_type
        self.vision = vision
        self.turn_counter = 0

    def behavior(self):
        self.turn_counter += 1
        rabbit = super().find_nearest('r')
        if rabbit != None:
            move = super().go_to(rabbit)
        else:
            move = super().random_move()
        super().move(move)
