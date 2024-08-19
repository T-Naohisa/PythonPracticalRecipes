import enum


class Nengo(enum.Enum):
    SHOWA = 1
    HEISEI = 2
    REIWA = 3


# 呼び出し
print(Nengo.SHOWA)
print(Nengo.HEISEI)
showa = Nengo.SHOWA
print(showa)
print(showa.name)
print(showa.value)


class Color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()

    def __str__(self):
        return self.name


def print_color(color: Color) -> None:
    print(color)


if __name__ == "__main__":
    print_color(Color.RED)
    print_color(Color.BLACK)
