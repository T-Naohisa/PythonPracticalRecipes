class MyOpenContextManeger:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print('__enter__:ファイルをopenします')
        self.file_obj = open(self.file_name, "r")
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print("__exit__:ファイルをcloseします")
        self.file_obj.close()


with MyOpenContextManeger("python.txt") as f:
    print(f.read())
