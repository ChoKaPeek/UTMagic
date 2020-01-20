import pygame
from engine.gameobject import GameObject
from game.cardinfo import CardInfo


class Card(GameObject):
    def __init__(self, symbol, color, power, sprite, coords, parent, app):
        self.symbol = symbol
        self.color = color
        self.power = power
        GameObject.__init__(self, sprite, coords, parent, app)
        self.info = CardInfo(self, self.transform, app)
        self.y_click = self.transform.local_y + 20
        self.y_base = self.transform.local_y

    def move_local_y(self, val):
        mouse_over = self.y_click == self.transform.local_y
        self.y_click = val + 20
        self.y_base = val
        self.transform.local_y = self.y_click if mouse_over else self.y_base

    def update(self, delta_time):
        GameObject.update(self, delta_time)
        x, y = self.app.mouse
        if self.rec.top < y < self.rec.bottom and self.rec.left < x < self.rec.right:
            self.transform.local_y = self.y_click
        elif not (self.transform.local_y == self.y_click and
                  self.rec.top - 21 < y < self.rec.bottom and
                  self.rec.left < x < self.rec.right):
            self.transform.local_y = self.y_base

    def draw(self, screen):
        GameObject.draw(self, screen)
