

class ScoreCard:


    def __init__(self, pins):
        self.pins = pins

    def get_pins(self):
        return self.pins

    @va
    def get_score(self):
        total = 0
        index = 0
        for i in range(10):
            if self.pins[index + 1] == "/":
                total += 10 + int(self.pins[index + 2]) 
                index += 2
            elif self.pins[index] == "X":
                total += 10 + int(self.pins[index + 1]) + int(self.pins[index + 2])
                index += 1
            else:
                if self.pins[index] != "-":  
                    total += int(self.pins[index])
                if self.pins[index + 1] != "-":
                    total += int(self.pins[index+1])
                    index += 2
        return total
    

    def __symbols_to_numbers(self):
        total = ""
        for i,pin in enumerate(self.pins):
            if pin == "-":
                total += "0"

            elif pin == "X":
                total += "10"

            elif pin == "/":
                total += str(10 - int(self.pins[i-1]))

            else:
                total += pin
        return total


    def __split_frames():
        


