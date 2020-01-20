from engine.gameobject import GameObject
from game.card import Card
import pygame


class Tape(GameObject):
    def __init__(self, cards, app):
        GameObject.__init__(self, None, (960, 100), None, app, -10)
        self.cards = []
        for c in cards:
            self.cards.append(Card(c, "green", 1, app.images[c + ".jpg"], (0, 0), self.transform, app))
        self.index = len(self.cards) // 2
        cursor = app.images["cursor.png"]
        GameObject(cursor, (-25, 220), self.transform, app, -2)
        GameObject(pygame.transform.flip(cursor, False, True), (-25, -60), self.transform, app, 10)

    def update(self, delta_time):
        GameObject.update(self, delta_time)
        for i in range(len(self.cards)):
            distance_head = i - self.index
            if distance_head <= 0:
                self.cards[i].color = "green"
                self.cards[i].power = -distance_head + 2
                if distance_head == 0:
                    self.cards[i].move_local_y(20)
            else:
                self.cards[i].color = "white"
                self.cards[i].power = distance_head + 3
            self.cards[i].transform.move_to((distance_head * 120 - 60, self.cards[i].transform.local_y), delta_time)

    def move_index(self, delta):
        self.index += delta
