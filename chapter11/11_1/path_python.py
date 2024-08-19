from pathlib import PurePath, Path

print(PurePath("samp.txt"))
print(PurePath("samp", "ham", "eggs.txt"))

p = Path()
print(p.cwd())
print(p.iterdir())
print(sorted(p.iterdir()))
for n in p.iterdir():
    print(n)
