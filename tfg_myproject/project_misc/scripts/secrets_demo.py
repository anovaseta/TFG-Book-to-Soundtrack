import string
import secrets
# alphabet = string.ascii_letters + string.digits
# password = ''.join(secrets.choice(alphabet) for i in range(8))
for _ in range(0,10):
    password = secrets.randbits(12)
    print(password)