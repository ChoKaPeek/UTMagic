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

    def draw(self, screen):
        GameObject.draw(self, screen)
