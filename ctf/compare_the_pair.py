import hashlib

salt = "f789bbc328a3d1a3"

i = 100000000

while 1:
    password = salt + str(i)
    password = password.encode('utf8')

    new_hash = hashlib.md5(password).hexdigest()
    if new_hash[0:2] == "0e" and new_hash[2:32].isdigit():
        print(password, str(i), new_hash)
        exit(0)
    i += 1
