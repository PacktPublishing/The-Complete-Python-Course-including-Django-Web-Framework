def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper

@my_decorator
def myfunc():
    print("My name is Kalob")

myfunc()
