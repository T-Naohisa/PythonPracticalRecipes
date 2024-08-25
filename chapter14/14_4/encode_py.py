import base64

s = "pythonは簡単に習得でき、それでいて強力な言語の1つです。"
enc_s = base64.b64encode(s.encode())
print(enc_s)

dec_s = base64.b64decode(enc_s).decode()
print(dec_s)
