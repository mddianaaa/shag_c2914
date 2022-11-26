import time


def fibonacci():
    b = c = 1


elements = [0, 1, 1]


for n in range(100):
    tmp = b + c
    b = c
    c = tmp
    elements.append(c)
print(elements)


def speed_test():
    t0 = time.time()
    fibonacci()
    t1 = time.time()
    total = t1-t0
    print(total)