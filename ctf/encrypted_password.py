from pwn import *
p = make_packer('all')

h = p(0x5A53010106040309)
h += p(0x5C585354500A5B00)
h += p(0x555157570108520D)
h += p(0x5707530453040752)

s = '875e9409f9811ba8560beee6fb0c77d2'
ans = ''

for x,y in zip(s,h):
    ans += chr(ord(x) ^ y)

print('247CTF{%s}' % ans)