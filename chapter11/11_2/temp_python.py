import tempfile
from pathlib import Path

with tempfile.TemporaryFile() as tmp:
    print(tmp.write(b"test test test\n"))
    print(tmp.seek(0))
    print(tmp.read())

    tmp.close()

tmpf = tempfile.NamedTemporaryFile()
print(tmpf.name)

p = Path(tmpf.name)
print(p.exists())
tmpf.close()
print(p.exists())
