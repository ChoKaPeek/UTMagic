from engine.transform import Transform


class GameObject:
    def __init__(self, sprite, coords, parent, app, layer=-1):
        self.transform = Transform(coords, parent)
        self.sprite = sprite
        if sprite:
            self.rec = sprite.get_rect()
        self.app = app
        self.layer = layer
        app.spawn(self)

    def update(self, delta_time):
        if self.sprite:
            self.rec.left, self.rec.top = self.transform.get_global_coords()

    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, self.rec)
