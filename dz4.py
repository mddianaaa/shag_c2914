class colorsize:
    eyes = "green"
    heir = "broun"
    def __init__(self):
        self.heenn = 168
        self.weenn = 60


class human(colorsize):
    def __init__(self):
        name = "Enn:"
        print(name)
        print(f"eyes: {self.eyes}")
        print(f"heir: {self.heir}")



class she(colorsize):
    def __init__(self):
        super().__init__()
        print(f"weight: {self.weenn}")
        print(f"height: {self.heenn}")
        car = "Laferari"
        job = "desinger"
        print(f"her job: {job}")
        print(f"her car: {car}")



en = human()
s = she()
print(en)
print(s)