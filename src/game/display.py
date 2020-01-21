import pygame
from engine.gameobject import GameObject


class Display(GameObject):
    def __init__(self, sprite, app):
        GameObject.__init__(self, sprite, (100, 100), None, app, layer=100)
        self.size = (444, 620)
        self.sprite = pygame.transform.scale(self.sprite, self.size)
        self.rec = self.sprite.get_rect()

    def update(self, delta_time):
        GameObject.update(self, delta_time)
        x, y = self.app.mouse
        if self.rec.top < y < self.rec.bottom and self.rec.left < x < self.rec.right and self.app.mouse_click:
            self.app.game_objects.remove(self)

    def draw(self, screen):
        GameObject.draw(self, screen)
