import pygame
import sys


class App:
    def __init__(self, size, background=(0, 0, 0)):
        pygame.init()
        self.size = size
        self.background = background
        self.screen = pygame.display.set_mode(self.size)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.background)
            pygame.display.flip()


if __name__ == '__main__':
    app = App((1000, 700))
    app.run()
