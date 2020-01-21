from engine.gameobject import GameObject


class Counter(GameObject):
    def __init__(self, text, coords, parent, app):
        GameObject.__init__(self, None, coords, parent, app)
        self.text = text
        self.count = 0
        self.text_display = self.app.font.render(f"{self.text}{self.count}", True, (200, 200, 200))
        self.rec_text = self.text_display.get_rect()

    def incr(self, incr=1):
        self.count += incr
        self.text_display = self.app.font.render(f"{self.text}{self.count}", True, (200, 200, 200))
        self.rec_text = self.text_display.get_rect()

    def draw(self, screen):
        self.rec_text.left, self.rec_text.top = self.transform.get_global_coords()
        screen.blit(self.text_display, self.rec_text)
