from engine.gameobject import GameObject
from game.card import Card


class Deck(GameObject):
    def __init__(self, coords, tape, parser, app):
        GameObject.__init__(self, app.images["back.jpg"], coords, None, app)
        self.tape = tape
        self.parser = parser
        self.change_state = False
        self.next_symbol = None
        self.offset = 0
        self.phase = -1
        self.cards = []
        self.cards.append(GameObject(app.images["infest.jpg"], (0, -330), self.transform, app))
        self.cards.append(GameObject(app.images["cleansing_beam.jpg"], (0, -330), self.transform, app))
        self.cards.append(GameObject(app.images["coalition_victory.jpg"], (0, -330), self.transform, app))
        self.cards.append(GameObject(app.images["eteigneurs_d_ames.jpg"], (0, -330), self.transform, app))
        for c in self.cards:
            c.active = False
        self.fast_mode = False

    def flip_mode(self):
        self.fast_mode = not self.fast_mode

    def update(self, delta_time):
        GameObject.update(self, delta_time)
        if self.fast_mode:
            self.next_phase()
        else:
            x, y = self.app.mouse
            if (self.app.mouse_click and
                    self.rec.left < x < self.rec.right and
                    self.rec.top < y < self.rec.bottom):
                self.next_phase()

    def next_phase(self):
        self.phase = (self.phase + 1) % 11
        if self.phase == 0:
            self.change_state, self.next_symbol, self.offset = self.parser.next()
            print(self.change_state, self.next_symbol, self.offset)
            self.tape.play_infest()
            self.cards[0].active = True
        if self.phase == 1:
            self.tape.read_head()
        if self.phase == 2:
            color = "green" if self.offset == 1 else "white"
            card = Card(self.next_symbol, color, 2, self.app.images[self.next_symbol + ".jpg"], (0, 0),
                        self.tape.transform, self.app)
            self.tape.write_head(card)
        if self.phase == 3:
            self.tape.remove_infest()
            self.cards[0].active = False
        if self.phase == 4:
            self.tape.play_cleansing()
            self.cards[1].active = True
        if self.phase == 5:
            self.cards[1].active = False
        if self.phase == 6:
            self.tape.play_coalition()
            self.cards[2].active = True
        if self.phase == 7:
            self.cards[2].active = False
            if self.change_state:
                self.phase = 9
        if self.phase == 8:
            self.tape.play_eteigneur()
            self.cards[3].active = True
        if self.phase == 9:
            self.cards[3].active = False
        if self.phase == 10:
            self.tape.move_index()
            if self.offset == 0:
                self.fast_mode = False
