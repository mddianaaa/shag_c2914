def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have a problem {exc}")
        else:
            print(f"No problem, Result = {result}")
    return checker

def calc(exppression):
    return eval(exppression)


calc = checker(calc)
calc("2+2")