from cube import Cube
from food import Food
import pygame as p
import sys
import random as r


class Game:

    running = True

    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((600, 600), 0, 32)
        p.display.set_caption('Snake')
        self.snake = []
        self.snake.append(Cube((0, 255, 0), 200, 200, 20, 20))
        self.clock = p.time.Clock()
        self.food = Food((255, 0, 0), (0, 29), (0, 29), 20, 20)    # color, rangeX, rangeY, sizeX, sizeY

    def execution(self):
        while True:
            Game.events(self)
            if Game.running:
                self.loop(self.clock)
                self.render()

    @staticmethod
    def events(self):
        for event in p.event.get():
            if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                sys.exit(0)
            elif event.type == p.KEYDOWN and event.key == p.K_w:
                self.snake[0].direction = 'up'
            elif event.type == p.KEYDOWN and event.key == p.K_s:
                self.snake[0].direction = 'down'
            elif event.type == p.KEYDOWN and event.key == p.K_a:
                self.snake[0].direction = 'left'
            elif event.type == p.KEYDOWN and event.key == p.K_d:
                self.snake[0].direction = 'right'
            elif event.type == p.KEYDOWN and event.key == p.K_SPACE:
                Game.switch_pause()

    @staticmethod
    def switch_pause():
        if Game.running:
            Game.running = False
        else:
            Game.running = True

    def loop(self, clock):
        clock.tick(4)
        if self.food.rect.colliderect(self.snake[0].rect):
            self.food.set_rect(r.randint(0, 29), r.randint(0, 29))
            if self.snake[0].direction == 'up':
                self.snake.append(Cube((0, 0, 255), 0, 0, 20, 20))
            elif self.snake[0].direction == 'down':
                self.snake.append(Cube((0, 0, 255), 0, 0, 20, 20))
            elif self.snake[0].direction == 'right':
                self.snake.append(Cube((0, 0, 255), 0, 0, 20, 20))
            elif self.snake[0].direction == 'left':
                self.snake.append(Cube((0, 0, 255), 0, 0, 20, 20))
        for i in range(1, len(self.snake)):
            if self.snake[0].rect.colliderect(self.snake[i].rect):
                sys.exit(0)  # WRÓCIC
        self.snake_move()

    def snake_move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].rect.x = self.snake[i-1].rect.x
            self.snake[i].rect.y = self.snake[i-1].rect.y

        if self.snake[0].direction == 'up':
            self.snake[0].rect.y = self.snake[0].rect.y - 20
        elif self.snake[0].direction == 'down':
            self.snake[0].rect.y = self.snake[0].rect.y + 20
        elif self.snake[0].direction == 'left':
            self.snake[0].rect.x = self.snake[0].rect.x - 20
        elif self.snake[0].direction == 'right':
            self.snake[0].rect.x = self.snake[0].rect.x + 20

    def render(self):
        self.screen.fill((122, 125, 128))
        for i in range(1, 30):
            p.draw.line(self.screen, (255, 255, 255), (i*20, 0), (i*20, 600), 1)
            p.draw.line(self.screen, (255, 255, 255), (0, i*20), (600, i*20), 1)
        for i in range(0, len(self.snake)):
            p.draw.rect(self.screen, self.snake[i].color, self.snake[i].rect)
        self.food.draw_food_rect(self.screen, self.food.color, self.food.rect)
        p.display.flip()


if __name__ == "__main__":
    snakeGame = Game()
    snakeGame.execution()
