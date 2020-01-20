import pygame
import sys
from os import listdir
from os.path import isfile, join


class App:
    def __init__(self, size, background=(0, 0, 0)):
        pygame.init()
        pygame.font.init()
        self.size = size
        self.background = background
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption('UTMagic')
        self.game_objects = []
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('FreeMono.ttf', 40)
        self.mouse = (0, 0)
        self.images = {}

    def load_images(self):
        all_names = [f for f in listdir("../images") if isfile(join("../images", f))]
        for name in all_names:
            self.images[name] = pygame.image.load(join("../images", name))

    def spawn(self, obj):
        self.game_objects.append(obj)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            delta_time = self.clock.tick()
            self.mouse = pygame.mouse.get_pos()
            self.screen.fill(self.background)
            for obj in self.game_objects:
                obj.update(delta_time)
                self.game_objects.sort(key=lambda obj: obj.layer)
                obj.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    app = App((1920, 1080), (20, 30, 50))
    app.load_images()
    app.run()
