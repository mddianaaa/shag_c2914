import random


class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannon build!"


def check_material(a, b):
    if a < b:
        num = random.randint(a, b)
        print(num)
    else:
        raise BuildingError()


a = int(input("chislo1: "))
b = int(input("chislo2: "))


check_material(a, b)