name: str = "123"
age: int = 18
favorite: dict = {"study": "プログラミング", "food": "バナナ"}


def greeting(name: str) -> str:
    """戻り値の方と異なる値を返す"""
    return f"Hi, {name}"


greeting("123")
