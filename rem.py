class Calc:
    def __init__(self):
        self.baseSize = input("Enter font base size: \n")

    def calc_loop(self):
        calcSize = ""
        while(calcSize != "No"):
            calcSize = input("Enter pixel: \n")
            print(self.calculate(calcSize))

    def calculate(self, px):
        rem = (float(px) / float(self.baseSize))

        return "Rem: \n\n" + str(rem) + "rem\n"