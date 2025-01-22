

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
            if self.pins[index + 1] == "/":
                total += ScoreCard.STRIKE + int(self.pins[index + 2]) 
                index += 2
            elif self.pins[index] == "X":
                total += ScoreCard.STRIKE + int(self.pins[index + 1]) + int(self.pins[index + 2])
                index += 1
            else:
                if self.pins[index] != "-":  
                    total += int(self.pins[index])
                if self.pins[index + 1] != "-":
                    total += int(self.pins[index+1])
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