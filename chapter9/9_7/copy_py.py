import copy

values = ["a", "b", "c", "d"]
val_cp = copy.copy(values)

print(val_cp)
val_cp[1] = "e"
print(val_cp)
print(values)
