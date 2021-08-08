import sys
import hashlib

password = bytes(sys.argv[1], 'utf-8')
h = hashlib.pbkdf2_hmac('sha512', password, b'Km5d5ivMy8iexuHcZrsD', 200000)

print(h.hex())
