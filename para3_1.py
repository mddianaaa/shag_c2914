class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []


    def addpassenger (self, human):
        self.passenger.append(human)

    def print_names_passenger(self):
        if self.passenger != []:
            print(f"Names {self.brand} passenger: ")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"no passenger in {self.brand}")


human1 = Human("Jack")
human2 = Human("Enn")

auto1 = Auto("Mercedes")
auto2 = Auto("Tatra")

auto1.print_names_passenger()
auto2.print_names_passenger()

auto1.addpassenger(human1)
auto2.addpassenger(human2)

auto1.print_names_passenger()
auto2.print_names_passenger()