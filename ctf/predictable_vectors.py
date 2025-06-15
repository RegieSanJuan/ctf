import requests
import binascii

IV = []
retrieved_flag = '64346436353162326136336433616339' #insert the value from 'Retrieved flag in hex:'
retrieved_flag_in_chr = 'd4d651b2a63d3ac9' #insert the value from 'Retrieved flag in chr:'

request_session = requests.Session()   
url = "https://b9ecec8fa88d822c.247ctf.com/" #place the host address
possiblities = ['61','62','63','64','65','66','30','31','32','33','34','35','36','37','38','39']
texts = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

def get_IV(converted_text):
    result = request_session.request('GET', url+'encrypt?plaintext='+converted_text)
    return result.text[-32:]

def xor_operation(a, b):
    xored = []
    for i in range(len(a)):
        xored_value = ord(a[i%len(a)]) ^ ord(b[i%len(b)])
        hex_value = hex(xored_value)[2:]
        if len(hex_value) == 1:
            hex_value = "0" + hex_value
        xored.append(hex_value)
    return ''.join(xored)

def sending_the_plaintext_after_XOR_2(possible_value,text,iteration_count):
    print('Count',count)
    global retrieved_flag
    global retrieved_flag_in_chr
    converted_text = binascii.hexlify(bytes(text, 'utf-8') * count).decode('utf-8')
    known_text = text*count

    IV = get_IV(converted_text)
    print('IV value:',IV)

    result1 = request_session.request('GET', url+'encrypt?plaintext='+converted_text)
    print(url+'encrypt?plaintext='+converted_text)
    print(result1.text)
    IV   = bytes.fromhex(IV).decode('latin-1')
    IV_2 = bytes.fromhex(result1.text[-32:]).decode('latin-1')
    xored_value1 = bytes.fromhex(xor_operation(IV, IV_2)).decode('latin-1')
    xored_value2 = xor_operation(xored_value1,known_text+retrieved_flag_in_chr[:iteration_count])
    result2 = request_session.request('GET', url+'encrypt?plaintext='+xored_value2+retrieved_flag[iteration_count*2:]+possible_value)
    print(url+'encrypt?plaintext='+xored_value2+retrieved_flag[iteration_count*2:]+possible_value)
    print(result2.text)
    print(possible_value)

    if(result1.text[32:64]==result2.text[32:64]):
        print('True')
        ascii_string = binascii.unhexlify(possible_value).decode('ascii')
        retrieved_flag_in_chr = retrieved_flag_in_chr + ascii_string
        retrieved_flag = retrieved_flag + possible_value
        return 'True'
    else:
        print('False')

count = 31 - int(len(retrieved_flag)/2)

for i in range(16):
    print('loop:',i+1)
    iteration_count = i+1
    for possibile_value,text in zip(possiblities,texts):
        result = sending_the_plaintext_after_XOR_2(possibile_value,text,iteration_count)
        if(result == 'True'):
            print('hi')
            count = count - 1
            break

print('Retrieved flag in Hex:',retrieved_flag)
print('Actual flag : 247CTF{'+ retrieved_flag_in_chr +'}')