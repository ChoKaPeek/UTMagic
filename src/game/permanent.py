import pygame
from engine.gameobject import GameObject
from game.display import Display


class Permanent(GameObject):
    def __init__(self, sprite, grid_pos, parent, app):
        self.size = (111, 155)
        coords = ((self.size[0] + 2) * grid_pos[0], (self.size[1] + 2) * grid_pos[1])
        GameObject.__init__(self, sprite, coords, parent, app)
        self.old_sprite = self.sprite
        self.sprite = pygame.transform.scale(self.sprite, self.size)
        self.rec = self.sprite.get_rect()

    def update(self, delta_time):
        GameObject.update(self, delta_time)
        x, y = self.app.mouse
        if self.rec.top < y < self.rec.bottom and self.rec.left < x < self.rec.right and self.app.mouse_click:
            Display(self.old_sprite, self.app)

    def draw(self, screen):
        GameObject.draw(self, screen)
