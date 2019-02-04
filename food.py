import cube
import pygame as p
import random as r


class Food(cube.Cube):

    def __init__(self, color, range_x, range_y, size_x, size_y):
        xa, xb = range_x
        ya, yb = range_y
        cube.Cube.__init__(self, color, r.randint(xa, xb), r.randint(ya, yb), size_x, size_y)

    def draw_food_rect(self):
        pass

    def init_rect_from_food(self):
        return p.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)


