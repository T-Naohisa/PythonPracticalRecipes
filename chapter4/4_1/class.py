class User:
    user_type = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        self.age += 1

    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""


user1 = User("寺田学", 35, "東京")
print(user1.age)
user1.increment_age()
print(user1.age)

print(user1.start_name)
