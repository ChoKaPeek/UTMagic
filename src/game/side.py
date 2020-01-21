from engine.gameobject import GameObject
from game.permanent import Permanent
import pygame


class Side(GameObject):
    def __init__(self, pos, permanents, grid, app):
        GameObject.__init__(self, None, pos, None, app, layer=-10)
        self.cards = []
        next_pos(grid)
        for p in permanents:
            self.cards.append(Permanent(app.images[p + ".jpg"], next_pos(), self.transform, app))

    def next_pos(grid=None):
        if grid:
            self.x = 0
            self.y = 0
            self.max_x = grid[0]
            self.max_y = grid[1]
        else:
            res = (self.x, self.y)
            self.x += 1
            if self.x == self.max_x:
                self.x = 0
                self.y += 1
                if self.y == self.max_y:
                    raise ValueError("Too many permanent cards for the grid")
            return res


    def update(self, delta_time):
        GameObject.update(self, delta_time)
