

class ScoreCard:

    STRIKE = 10

    def __init__(self, pins):
        self.pins = pins

    def get_pins(self):
        return self.pins

    def get_score(self):
        total = 0
        index = 0
        for i in range(10):
            if self.get_pins()[index + 1] == "/" and index + 2 < len(self.get_pins()):
                total += ScoreCard.STRIKE + int(self.get_pins()[index + 2]) 
                index += 2
            elif self.get_pins()[index] == "X" and index + 3 < len(self.get_pins()):
                total += ScoreCard.STRIKE + int(self.get_pins()[index + 1]) + int(self.get_pins()[index + 2])
                index += 1
            else:
                if self.get_pins()[index] != "-":  
                    total += int(self.get_pins()[index])
                if self.get_pins()[index + 1] != "-":
                    total += int(self.get_pins()[index+1])
                    index += 2
        return total
    

    def symbols_to_numbers(self):
        total = ""
        for i,pin in enumerate(self.pins):
            if pin == "-":
                total += "0"

            elif pin == "X":
                total += "10"

            elif pin == "/":
                total += str(ScoreCard.STRIKE - int(self.pins[i-1]))

            else:
                total += pin
        return total


    def split_frames(self):

        rolls_splited = list(self.pins)
        total_frames = []
        index = 0
        for i in range(10):
            if len(total_frames) ==  8:
                total_frames.append([rolls_splited[i:]])

            else:
                total_frames.append([rolls_splited[i],rolls_splited[i+1]])
                index +=2

        return total_frames