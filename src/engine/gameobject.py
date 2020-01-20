from engine.transform import Transform


class GameObject:
    def __init__(self, sprite, coords, parent, app):
        self.transform = Transform(coords, parent)
        if sprite:
            self.rec = sprite.get_rect()
            self.sprite = sprite
        self.app = app
        app.spawn(self)

    def update(self, delta_time):
        pass

    def draw(self, screen):
        self.rec.left, self.rec.top = self.transform.get_global_coords()
        screen.blit(self.sprite, self.rec)
