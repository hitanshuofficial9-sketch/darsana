def my_decorator(func):
    def wrapper():
        print("something before function")

        func()
        print("something after function")
    return wrapper
    
@my_decorator
def say_hello():
    print("hello")

say_hello()
