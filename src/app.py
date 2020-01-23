import pygame
import sys
from os import listdir
from os.path import isfile, join
from game.tape import Tape
from game.side import Side
from game.deck import Deck
from main import Handler


class App:
    def __init__(self, argv, size, background=(0, 0, 0)):
        pygame.init()
        pygame.font.init()
        self.argv = argv
        self.size = size
        self.background = background
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption('UTMagic')
        self.game_objects = []
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('FreeMono.ttf', 40)
        self.mouse = (0, 0)
        self.mouse_click = False
        self.images = {}
        self.tape = None
        self.deck = None

    def load_images(self):
        all_names = [f for f in listdir("../images") if isfile(join("../images", f))]
        for name in all_names:
            self.images[name] = pygame.image.load(join("../images", name))

    def init_game(self):
        Side((565, 50), ["rotlung_reanimator",
                         "necromancien_de_xathrid", "wild_evocation", "recycle",
                         "privileged_position", "vigor", "archonte_brulant"], (7, 1), self)
        Side((565, 730), ["rotlung_reanimator", "cloak_of_invisibility",
                          "roue_du_soleil_et_de_la_lune", "gains_illusoires", "fungus_sliver",
                          "steely_resolve", "dread_of_night", "shared_triumph", "vigor",
                          "archonte_brulant", "ancient_tomb", "mesmeric_orb",
                          "augure_prismatique", "choke"], (7, 2), self)
        handler = Handler(self.argv)
        self.tape = Tape(handler.get_init(), (960, 360), self)
        # state_changed, symbol, direction = handler.next() # bool, char, int
        self.deck = Deck((1600, 650), self.tape, handler, self)

    def spawn(self, obj):
        self.game_objects.append(obj)

    def handle_input(self):
        self.mouse = pygame.mouse.get_pos()
        self.mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.deck.flip_mode()
                if event.key == pygame.K_LEFT:
                    self.tape.index = 0
                if event.key == pygame.K_RIGHT:
                    self.deck.next_phase()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True

    def run(self):
        while True:
            self.handle_input()
            delta_time = self.clock.tick()
            self.screen.fill(self.background)
            for obj in self.game_objects:
                obj.update(delta_time)
                self.game_objects.sort(key=lambda o: o.layer)
                obj.draw(self.screen)
            pygame.display.flip()


if __name__ == '__main__':
    app = App(sys.argv, (1920, 1080), (20, 30, 50))
    app.load_images()
    app.init_game()
    app.run()
