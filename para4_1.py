class Human:
    height = 160


class Student(Human):
    pass


class Worker(Human):
    pass


Enn = Student()
Lisa = Worker()
Rose = Student()

print(Enn.height)
print(Lisa.height)
print(Rose.height)

