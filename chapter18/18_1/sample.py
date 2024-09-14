import secrets
import string

ahpha_num = string.ascii_letters + string.digits
print(ahpha_num)

password = "".join(secrets.choice(ahpha_num) for i in range(8))
print(password)
