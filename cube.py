import pygame as p


class Cube:

    def __init__(self, color, pos_x, pos_y, size_x, size_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.rect = p.Rect(pos_x, pos_y, size_x, size_y)
        self.direction = ''

    def init_rect_from_cube(self):
        return p.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)
