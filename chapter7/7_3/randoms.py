import random


# ランダム生成
print(random.random())

# ランダム1～10
print(random.randint(1, 10))

num_list = [1, 2, 3]
print(random.choice(num_list))
print(random.choices(num_list, 2))
