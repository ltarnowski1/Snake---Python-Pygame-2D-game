import cube
import pygame as p
import random as r


class Food(cube.Cube):

    def __init__(self, color, range_x, range_y, size_x, size_y):
        Food.set_random_food_position(self, range_x, range_y)
        cube.Cube.__init__(self, color, self.pos_x, self.pos_y, size_x, size_y)

    def draw_food_rect(self, screen, color, rect):
        p.draw.rect(screen, color, rect)

    def set_rect(self, pos_x, pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_random_food_position(self, range_x, range_y):
        xa, xb = range_x
        ya, yb = range_y
        random_x = r.randint(xa, xb)
        random_y = r.randint(ya, yb)
        self.pos_x = random_x
        self.pos_y = random_y


