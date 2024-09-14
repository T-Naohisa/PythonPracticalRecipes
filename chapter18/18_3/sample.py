import cryptography
from cryptography.fernet import Fernet

# 共通かぎの生成
key = Fernet.generate_key()
print(key)

cipher = Fernet(key)
print(cipher)

# 暗号化
cipher_text = cipher.encrypt(b"It is a really secret message")
print(cipher_text)

# 複合化
print(cipher.decrypt(cipher_text))
