class Clas1:
    var = 20
    def __init__(self):
        self.var = 10


class Clas2(Clas1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)


hello_world = Clas2()
hw = Clas1()
print(hw.var)