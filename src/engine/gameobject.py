from Engine.transform import Transform


class GameObject:
    def __init__(self, sprite, coords=(0, 0), parent=None):
        self.transform = Transform(coords, parent)
        self.rec = sprite.get_rect()
        self.sprite = sprite

    def update(self, delta_time):
        pass

    def draw(self, screen):
        self.rec.top, self.rec.left = self.transform.get_global_coords()
        screen.blit(self.sprite, self.rec)
