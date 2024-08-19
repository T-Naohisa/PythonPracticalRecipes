import random
from retrying import retry


@retry
def my_func():
    if random.randint(0, 10) == 5:
        print("5です")
    else:
        print("raise ValueError")
        raise ValueError("5ではありません")


my_func()
