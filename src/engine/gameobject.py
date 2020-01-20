from engine.transform import Transform


class GameObject:
    def __init__(self, sprite, coords, parent, app, layer=-1):
        self.transform = Transform(coords, parent)
        if sprite:
            self.rec = sprite.get_rect()
            self.sprite = sprite
        self.app = app
        self.layer = layer
        app.spawn(self)

    def update(self, delta_time):
        self.rec.left, self.rec.top = self.transform.get_global_coords()

    def draw(self, screen):
        screen.blit(self.sprite, self.rec)
