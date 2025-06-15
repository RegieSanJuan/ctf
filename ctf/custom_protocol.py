URL="34348b76f90c14d2.247ctf.com"
PORT=50470

from pwn import *

import binascii
import codecs


# Connect to the server
conn = remote(URL,PORT)

# remove \r\n from sessionID as we will add bytes to the packet
sessionID = conn.recvline()[:-2]

# define separator, counter, command and end
sep = b'00' # separator
counter = b'31'
command = b'34'
end = b'\r\n'

# Request format:
# sessionID 00 counter 00 command 00 redundancy \r\n

# calculate CRC redundancy
redundancy = binascii.crc32(binascii.a2b_hex(sessionID+sep+counter+sep+command))
red = b''
for i in str(redundancy):
    red += codecs.encode(str.encode(i), 'hex')

# create payload
payload = sessionID+sep+counter+sep+command+sep+red+end

conn.send(payload)
#print (payload)
response = conn.recvline()
#print (response)
print (unhex(response))

conn.close()
