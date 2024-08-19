import io

stream = io.StringIO("abcdefghijk")
print(stream.read(5))
print(stream.tell())
print(stream.read(5))
print(stream.tell())

stream.seek(0, io.SEEK_END)
stream.write("test")
print(stream.getvalue())

stream.close()
