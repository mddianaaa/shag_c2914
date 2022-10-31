try:
    try:
        print("start")
        print(hello)
        print("End. No error")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)