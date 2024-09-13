import hashlib

print(hashlib.algorithms_available)

hash_sha256 = hashlib.sha256()
hash_sha256.update(b"Python library book 2")
print(hash_sha256.hexdigest())
