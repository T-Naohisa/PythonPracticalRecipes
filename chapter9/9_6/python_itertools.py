import itertools

it = itertools.chain(["A", "B"], "ab", range(3))
for element in it:
    print(element)

for value, group in itertools.groupby("1231233"):
    print(f"{value}: {list(group)}")


it1 = (1, 2, 3, 4, 5)
it2 = ["abc", "ABC", "123"]
for v in itertools.zip_longest(it1, it2, fillvalue="-"):
    print(v)
