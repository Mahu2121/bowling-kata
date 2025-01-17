

class ScoreCard:


    def __init__(self, pins):
        self.pins = pins

    def get_pins(self):
        
        return self.pins

    def get_score_card_result(self,pins):
        total = 0
        for i in range(len(pins)):
            if pins[i].isdigit():
                total += int(pins[i])
        return total
        