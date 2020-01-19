import pygame
import sys
from os import listdir
from os.path import isfile, join


class App:
    def __init__(self, size, background=(0, 0, 0)):
        pygame.init()
        self.size = size
        self.background = background
        self.screen = pygame.display.set_mode(self.size)
        self.game_objects = []
        self.clock = pygame.time.Clock()
        self.images = {}

    def load_images(self):
        all_names = [f for f in listdir("../images") if isfile(join("../images", f))]
        for name in all_names:
            self.images[name] = pygame.image.load("../images/" + name)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.background)
            for obj in self.game_objects:
                obj.update(self.clock.get_time)
                obj.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    app = App((1000, 700))
    app.load_images()
    app.run()
