import pygame
import sys


class Game:

    running = True
    direction = ''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.head = pygame.Rect(100, 100, 20, 20)

    def execution(self):
        while True:
            Game.events()
            if Game.running:
                self.loop()
                self.render()

    @staticmethod
    def events():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                Game.direction = 'up'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                Game.direction = 'down'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                Game.direction = 'left'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                Game.direction = 'right'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Game.switch_pause()

    def loop(self):
        self.snake_move()

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 150, 255), self.head)
        pygame.display.flip()

    def snake_move(self):
        if Game.direction == 'up':
            self.head = self.head.move(0, -1)
        elif Game.direction == 'down':
            self.head = self.head.move(0, 1)
        elif Game.direction == 'left':
            self.head = self.head.move(-1, 0)
        elif Game.direction == 'right':
            self.head = self.head.move(1, 0)

    @staticmethod
    def switch_pause():
        if Game.running:
            Game.running = False
        else:
            Game.running = True


if __name__ == "__main__":
    snakeGame = Game()
    snakeGame.execution()
