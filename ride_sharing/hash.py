import hashlib

pwd = "Onu"
pwd_encode = pwd.encode()
pwd_encrypted = hashlib.md5(pwd_encode).hexdigest()
print(pwd_encrypted)
