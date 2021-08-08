import sys
import hashlib
import os

password = bytes(sys.argv[1], 'utf-8')

h = hashlib.pbkdf2_hmac('sha512', password, os.urandom(20), 200000)

sha512_hash = hashlib.sha512()
sha512_hash.update(h)

print(sha512_hash.hexdigest())
