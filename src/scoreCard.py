

class ScoreCard:


    def __init__(self, pins):
        self.pins = pins

    def get_pins(self):
        return self.pins

    def get_score(self):
        total = 0
        for pin in self.pins:
            if pin.isdigit():
                total += int(pin)
        return total
