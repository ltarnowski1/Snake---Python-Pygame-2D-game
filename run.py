from food import Food
import pygame as p
import sys


class Game:

    running = True
    direction = ''

    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((600, 600), 0, 32)
        p.display.set_caption('Snake')
        self.head = p.Rect(100, 100, 20, 20)
        self.clock = p.time.Clock()
        self.food = Food((255, 0, 0), (0, 580), (0, 580), 20, 20)    # color, rangeX, rangeY, sizeX, sizeY
        self.foodRect = self.food.init_rect_from_food()

    def execution(self):
        while True:
            Game.events()
            if Game.running:
                self.loop(self.clock)
                self.render()

    @staticmethod
    def events():
        for event in p.event.get():
            if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                sys.exit(0)
            elif event.type == p.KEYDOWN and event.key == p.K_w:
                Game.direction = 'up'
            elif event.type == p.KEYDOWN and event.key == p.K_s:
                Game.direction = 'down'
            elif event.type == p.KEYDOWN and event.key == p.K_a:
                Game.direction = 'left'
            elif event.type == p.KEYDOWN and event.key == p.K_d:
                Game.direction = 'right'
            elif event.type == p.KEYDOWN and event.key == p.K_SPACE:
                Game.switch_pause()

    @staticmethod
    def switch_pause():
        if Game.running:
            Game.running = False
        else:
            Game.running = True

    def loop(self, clock):
        clock.tick(150)
        if self.foodRect.colliderect(self.head):
            print('KOLIZJA')
            del self.foodRect, self.food
            self.food = Food((255, 0, 0), (0, 580), (0, 580), 20, 20)
            self.foodRect = self.food.init_rect_from_food()
        self.snake_move()

    def snake_move(self):
        if Game.direction == 'up':
            self.head = self.head.move(0, -1)
        elif Game.direction == 'down':
            self.head = self.head.move(0, 1)
        elif Game.direction == 'left':
            self.head = self.head.move(-1, 0)
        elif Game.direction == 'right':
            self.head = self.head.move(1, 0)

    def render(self):
        self.screen.fill((0, 0, 0))
        p.draw.rect(self.screen, self.food.color, self.foodRect)
        p.draw.rect(self.screen, (0, 150, 255), self.head)
        p.display.flip()


if __name__ == "__main__":
    snakeGame = Game()
    snakeGame.execution()
