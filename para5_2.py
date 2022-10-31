import inspect
import sys

data = "string"

def human():
    pass


def data2():
    pass



data = data2
print(inspect.ismodule(human))
print(inspect.isclass(human))
print(inspect.isfunction(human))

print(sys.executable)
print(sys.platform)
print(sys.version)