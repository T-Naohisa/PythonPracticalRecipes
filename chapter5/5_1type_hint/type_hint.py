from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Book:
    name: str
    author: str
    price: int


def books_a_bargain(book_list: list[Book]) -> Book:
    """ priceでソートして一番安い本を返す """
    return sorted(book_list, key=attrgetter("price"))[0]


py_book = [
    Book("ハッカーガイド", "terayon", 2992),
    Book("ゼロから", "takanori", 3200),
    Book("スタートブック", "shingo", 2750)
]
value_book: Book = books_a_bargain(py_book)
print(value_book)


def say_hello(name: str) -> str:
    return f"hello, {name}"


name: str = "TypeHint-kun"
message = say_hello(name)
print(message)
