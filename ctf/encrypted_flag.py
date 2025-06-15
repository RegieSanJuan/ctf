from Crypto.Protocol.KDF import PBKDF1
from Crypto.Cipher import AES
import hashlib

def decrypt_aes_256_cbc(data, password, salt):
    key_iv = hashlib.md5(password.encode() + salt).digest()
    # OpenSSL key derivation uses MD5 and repeats
    key = key_iv
    iv = salt  # For OpenSSL salted encryption, IV is next 16 bytes after salt, but this is simplified
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(data)
    return decrypted

def try_password(password, enc_file):
    with open(enc_file, 'rb') as f:
        data = f.read()
    if data[:8] != b'Salted__':
        print("No salt found!")
        return False
    salt = data[8:16]
    encrypted = data[16:]
    try:
        decrypted = decrypt_aes_256_cbc(encrypted, password, salt)
        # crude check for printable ASCII in decrypted output:
        if all(32 <= b < 127 for b in decrypted[:20]):
            print(f"Possible password: {password}")
            print("Decrypted sample:", decrypted[:50])
            return True
    except Exception as e:
        return False
    return False

def brute_force(wordlist_file, enc_file):
    with open(wordlist_file, 'r', encoding='latin1') as f:
        for line in f:
            password = line.strip()
            if try_password(password, enc_file):
                print(f"Success! Password is: {password}")
                break

if __name__ == '__main__':
    brute_force('rockyou.txt', 'encrypted_flag.enc')
