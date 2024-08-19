import sys

# print(sys.path)


# print(sys.stdout.write("standard output message"))
# print(sys.stderr.write("standard error message"))
# sys.stdin.read()
def print_hello():
    print("Hello")


sys.breakpointhook = print_hello

if __name__ == "__main__":
    print("start")
    breakpoint()
    print("end")
