import traceback


def hoge():
    tuple()[0]


try:
    hoge()
except IndexError:
    print("--- Exception occured ---")
    traceback.print_exc(limit=1)
