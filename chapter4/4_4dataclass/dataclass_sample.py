from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    address: int
    active: bool = False


# init等の特殊メソッドは自動で定義される
user = User("manabu", 60, "Chiba")
print(user.address)
user.age = 50
print(user.age)
