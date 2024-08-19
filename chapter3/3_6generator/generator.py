# ジェネレーターのサンプル
def multipulier(values):
    for i in values:
        yield 2 ** i  # ここで処理がとまる
        print("yield後")


values = [1, 2, 3, 4, 5]
ret = multipulier(values)
for value in ret:
    print(value)
    print("value")
