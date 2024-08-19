from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrap_function(a):
        """wraps_functionのドキュメントです"""
        func(a)
    return wrap_function


@my_decorator
def greeting(name):
    """greetingのドキュメントです"""
    print(f"こんにちわ、{name}さん")


print(greeting.__name__)
print(greeting.__doc__)
greeting("Tom")
