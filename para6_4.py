class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannon build!"


def check_material(material1, limit):
    if material1 >= limit:
        print("Go!")
    else:
        raise BuildingError()


materials = 400
limits = 450

check_material(materials, limits)