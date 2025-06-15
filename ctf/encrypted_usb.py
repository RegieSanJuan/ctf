import os
import itertools

# Define the PNG magic bytes
png_magic_bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

# Define the character space for the password
character_space = 'abcdefghijklmnopqrstuvwxyz'

# Generate all possible combinations of the password
# We know that the passwords is 4 lowercase characters
passwords = itertools.product(character_space, repeat=4)

# Path to the encrypted file
encrypted_file = 'do_not_open.png.xxx.crypt'
#encrypted_file = 'crypto_passphrase.png.xxx.crypt'
#encrypted_file = 'meeting_minutes.png.xxx.crypt'
#encrypted_file = 'passwords.png.xxx.crypt'
#encrypted_file = 'salary_screenshot.png.xxx.crypt'


# Path to save the decrypted file
decrypted_file = 'do_not_open.png'
#decrypted_file = 'crypto_passphrase.png'
#decrypted_file = 'meeting_minutes.png'
#decrypted_file = 'passwords.png'
#decrypted_file = 'salary_screenshot.png'

# Function to perform XOR encryption on a file with a given password
def xor_encrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        file_bytes = file.read()

    password_bytes = password.encode()
    encrypted_bytes = bytearray()

    for i, byte in enumerate(file_bytes):
        encrypted_byte = byte ^ password_bytes[i % len(password_bytes)]
        encrypted_bytes.append(encrypted_byte)

    return encrypted_bytes

# Read the first 8 bytes from the encrypted file
with open(encrypted_file, 'rb') as f:
    encrypted_bytes = f.read(8)

# Iterate through each password combination and check if it decrypts the file successfully
for password in passwords:
    password_str_4char = ''.join(password)
    # We need 8 bytes long password for test XOR
    password_str = password_str_4char+password_str_4char
    decrypted_bytes = b''

    # XOR each byte with the corresponding byte from the password
    for i in range(8):
        decrypted_byte = encrypted_bytes[i] ^ ord(password_str[i])
        decrypted_bytes += bytes([decrypted_byte])

    # Check if the decrypted bytes match the PNG magic bytes
    if decrypted_bytes == png_magic_bytes:
        print(f"Correct password found: {password_str_4char}")
        print(f"Decrypted file saved as: {decrypted_file}")
        # Decrypt the encrypted file using the current password
        decrypted_bytes = xor_encrypt_file(encrypted_file, password_str_4char)

        # Write the decrypted bytes to a file
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted_bytes)
        break