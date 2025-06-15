from pwn import *

url = '59cf3e5353abad13.247ctf.com'
port = '50023'

client = remote(url, port)

print(client.recvline())
print(client.recvline())
for i in range(500):
    problem = client.recvline().decode("utf-8")
    
    indexing = problem.split()

    Qa = int(indexing[5])
    Qb = int(indexing[7].strip('?'))
    answer = (str(Qa+Qb)+ '\r\n').encode("utf-8")
    print(f'answering {i} question ({Qa ,"+", Qb})...')
    client.sendline(answer)
    client.recvline()
flag = client.recvline().decode("utf-8").strip('\r\n')

print("Catched the flag!",flag)

client.close()