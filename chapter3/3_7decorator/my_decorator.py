def my_decorator(func):
    def wrap_function():
        func()
        print(f"function: {func.__name__} called")
    return wrap_function


def greeting():
    print("こんにちわ")


greeting = my_decorator(greeting)
print(greeting)
greeting()
