import contextlib


@contextlib.contextmanager
def my_open_contextmanager(file_name):
    file_obj = open(file_name, "r")
    try:
        print("__enter__:ファイルをopenします")
        yield file_obj
    except Exception as e:
        print(f"__enter__:{type(e)}")
        raise
    finally:
        file_obj.close()
        print("__exit__:ファイルをcloseします")


with my_open_contextmanager("python.txt") as f:
    print(f.read())
