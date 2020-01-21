import pygame
from engine.gameobject import GameObject


class CardInfo(GameObject):
    def __init__(self, card, parent, app):
        GameObject.__init__(self, None, (55, 140), parent, app)
        self.card = card
        self.last_power = card.power
        self.text_power = self.app.font.render(f"{self.card.power} / {self.card.power}", True, (10, 10, 10))
        self.rec_power = self.text_power.get_rect()
        self.text_symbol = self.app.font.render(self.card.symbol, True, (10, 10, 10))
        self.rec_symbol = self.text_symbol.get_rect()

    def update(self, delta_time):
        if self.last_power != self.card.power:
            self.last_power = self.card.power
            self.text_power = self.app.font.render(f"{self.card.power} / {self.card.power}", True, (10, 10, 10))
            self.rec_power = self.text_power.get_rect()

    def draw(self, screen):
        global_coords = self.transform.get_global_coords()
        color = (50, 200, 100) if self.card.color == "green" else (200, 200, 200)
        pygame.draw.circle(screen, color, global_coords, 40)
        self.rec_power.center = (global_coords[0], global_coords[1] - 15)
        self.rec_symbol.center = (global_coords[0], global_coords[1] + 15)
        screen.blit(self.text_power, self.rec_power)
        screen.blit(self.text_symbol, self.rec_symbol)
