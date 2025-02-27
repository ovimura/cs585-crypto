# CS585: Cryptography
# Student: Ovidiu Mura
# Assignment: Project 1
# Date: Jan 20, 2020

import sys

plaintext_file = None
ciphertext_file = None
key_file = None

bit_bock_size = 64
bit_key_size = 80
round_num = 0

ws = {}
cs = {}
key = {}
rs = {}
keys = []
key_str = None
new_key = 0
current_used_keys = {}

ftable = [[0xa3,0xd7,0x09,0x83,0xf8,0x48,0xf6,0xf4,0xb3, 0x21,0x15,0x78,0x99,0xb1,0xaf,0xf9],
[0xe7,0x2d,0x4d,0x8a,0xce,0x4c,0xca,0x2e,0x52,0x95,0xd9,0x1e,0x4e,0x38,0x44,0x28],
[0x0a,0xdf,0x02,0xa0,0x17,0xf1,0x60,0x68,0x12,0xb7,0x7a,0xc3,0xe9,0xfa,0x3d,0x53],
[0x96,0x84,0x6b,0xba,0xf2,0x63,0x9a,0x19,0x7c,0xae,0xe5,0xf5,0xf7,0x16,0x6a,0xa2],
[0x39,0xb6,0x7b,0x0f,0xc1,0x93,0x81,0x1b,0xee,0xb4,0x1a,0xea,0xd0,0x91,0x2f,0xb8],
[0x55,0xb9,0xda,0x85,0x3f,0x41,0xbf,0xe0,0x5a,0x58,0x80,0x5f,0x66,0x0b,0xd8,0x90],
[0x35,0xd5,0xc0,0xa7,0x33,0x06,0x65,0x69,0x45,0x00,0x94,0x56,0x6d,0x98,0x9b,0x76],
[0x97,0xfc,0xb2,0xc2,0xb0,0xfe,0xdb,0x20,0xe1,0xeb,0xd6,0xe4,0xdd,0x47,0x4a,0x1d],
[0x42,0xed,0x9e,0x6e,0x49,0x3c,0xcd,0x43,0x27,0xd2,0x07,0xd4,0xde,0xc7,0x67,0x18],
[0x89,0xcb,0x30,0x1f,0x8d,0xc6,0x8f,0xaa,0xc8,0x74,0xdc,0xc9,0x5d,0x5c,0x31,0xa4],
[0x70,0x88,0x61,0x2c,0x9f,0x0d,0x2b,0x87,0x50,0x82,0x54,0x64,0x26,0x7d,0x03,0x40],
[0x34,0x4b,0x1c,0x73,0xd1,0xc4,0xfd,0x3b,0xcc,0xfb,0x7f,0xab,0xe6,0x3e,0x5b,0xa5],
[0xad,0x04,0x23,0x9c,0x14,0x51,0x22,0xf0,0x29,0x79,0x71,0x7e,0xff,0x8c,0x0e,0xe2],
[0x0c,0xef,0xbc,0x72,0x75,0x6f,0x37,0xa1,0xec,0xd3,0x8e,0x62,0x8b,0x86,0x10,0xe8],
[0x08,0x77,0x11,0xbe,0x92,0x4f,0x24,0xc5,0x32,0x36,0x9d,0xcf,0xf3,0xa6,0xbb,0xac],
[0x5e,0x6c,0xa9,0x13,0x57,0x25,0xb5,0xe3,0xbd,0xa8,0x3a,0x01,0x05,0x59,0x2a,0x46]]

INT_BITS = 80


def leftRotate(n, d):
    return (n << d)|(n >> (INT_BITS - d))

def print_input_file_names():
    print("plaintext file name: {}".format(plaintext_file))
    print("key file name: {}".format(key_file))

def read_plaintext(file):
    global ws
    with open(file) as f:
        data = f.read()
    s = "".join("0x{:02x} ".format(ord(c)) for c in data)
    d = data.encode()[:-1]
    x = 8
    idx = 0
    temp = []
    for i in range(0,len(d), 2):
        ws[idx] = []
        x = len(d)%2 if(len(d)<i+x) else 2
        for j in range(i, i+x):
            temp.append(d[j])
        ws[idx] += (temp)
        idx += 1
        temp.clear()
    return s

def read_ciphertext(file='ciphertext.txt'):
    global cs
    c_str = ''
    with open(file,'r') as f:
        data = f.read()
    if(data[:2] == '0x'):
        c_str = data[2:] #-1]
    else:
        c_str = data#[:-1]
    s = "".join("0x{:02x} ".format(ord(c)) for c in c_str)
    d = c_str.encode()[:-1] if len(c_str.encode()) % 16 != 0 else c_str.encode()

    x = 16
    idx = 0
    temp = []
    for i in range(0,len(d), 4):
        cs[idx] = []
        x = len(d) % 4 if(len(d)<i+x) else 4
        for j in range(i, i+x,2):
            #print(d[j:j+2])
            temp.append(int(d[j:j+2],16))
        cs[idx] += (temp)
        idx += 1
        temp.clear()
    return s

def read_key(file):
    global key
    with open(file) as f:
        data = f.read()
    s = "".join("0x{:02x} ".format(ord(c)) for c in data)
    d = data.encode()[:-1]
    x = 8
    idx = 0
    temp = []
    for i in range(0,len(d), 2):
        key[idx] = []
        x = len(d)%2 if(len(d)<i+x) else 2
        for j in range(i, i+x):
            temp.append(d[j])
        key[idx] += (temp)
        idx += 1
        temp.clear()
    print('key')
    print(s)
    print("".join("0x{:02x} ".format(ord(x)) for x in data))
    return data

# https://www.allkeysgenerator.com/Random/Security-Encryption-Key-Generator.aspx
def read_hex_to_key(file='key.txt'):
    global key
    global key_str
    with open(file) as f:
            data = f.read()
    if(data[:2] == '0x'):
        key_str = data[2:-1]
    else:
        key_str = data[:-1]
    li = []
    for i in range(0,len(key_str),2):
        li.append(key_str[i:i+2])
    x = 8
    idx = 0
    temp = []
    for i in range(0,len(li), 2):
        key[idx] = []
        x = len(li)%2 if(len(li)<i+x) else 2
        for j in range(i, i+x):
            temp.append(li[j])
        key[idx] += (temp)
        idx += 1
        temp.clear()
    return key_str

read_hex_to_key()

def encrypt_0():
    global round_num
    global ws
    global key
    global current_used_keys
    global ciphertext_file
    global rs
    temp = []
    for i in range(4):
        w = ws[i]
        k = key[i]
        rs[i] = []
        for j in range(2):
            temp.append(w[j] ^ int(k[j],16))
        rs[i] += temp
        temp.clear()
    round_num = 0
    R0 = rs[0]
    R1 = rs[1]
    R2 = rs[2]
    R3 = rs[3]
    rr0 = None
    rr1 = None
    rr2 = None
    rr3 = None
    print('\nENCRYPTION')
    for _ in range(20):
        current_used_keys[round_num] = []
        print('\nBeginning of Round: {}'.format(round_num))
        F0, F1 = F(R0, R1, round_num)
        PREV_R0 = R0
        PREV_R1 = R1
        R0 = int('{:02x}{:02x}'.format(R2[0],R2[1]),16) ^ F0 # next R0
        R1 = int('{:02x}{:02x}'.format(R3[0],R3[1]),16) ^ F1 # next R1
        R2 = [int('{:04x}'.format(R0)[0:2],16), int('{:04x}'.format(R0)[2:4],16)]
        R3 = [int('{:04x}'.format(R1)[0:2],16), int('{:04x}'.format(R1)[2:4],16)]
        R0 = R2
        R1 = R3
        print('Subkeys used:', end=" ")
        y = ''
        [print("0x{} ".format(x),end=" ") for x in current_used_keys[round_num]]
        y0 = R2
        y1 = R3
        y2 = PREV_R0
        y3 = PREV_R1

        rr0 = y2
        rr1 = y3
        rr2 = y0
        rr3 = y1

        R2 = PREV_R0
        R3 = PREV_R1
        cipher = '{:02x}{:02x}'.format(y0[0],y0[1]) + '{:02x}{:02x}'.format(y1[0],y1[1]) + '{:02x}{:02x}'.format(y2[0],y2[1]) + '{:x}{:x}'.format(y3[0],y3[1])
        print('\nBlock: 0x{}'.format(cipher))
        print('End of Round: {}'.format(round_num))
        round_num += 1
    yy0 = rr0
    yy1 = rr1
    yy2 = rr2
    yy3 = rr3
    cipher = '{:02x}{:02x}'.format(yy0[0],yy0[1]) + '{:02x}{:02x}'.format(yy1[0],yy1[1]) + '{:02x}{:02x}'.format(yy2[0],yy2[1]) + '{:x}{:x}'.format(yy3[0],yy3[1])
    temp = []
    c = {}
    m = 4
    idx = 0
    for i in range(0,16,4):
        w = cipher[i:(i+4)]
        k = key[(i-m)%4]
        m-=1
        c[idx] = []
        id = 0
        for j in range(0,4,2):
            temp.append(int(w[j:(j+2)],16) ^ int(k[id],16))
            id+=1
        c[idx] += temp
        idx+=1
        temp.clear()
    cc = ''
    for n in range(4):
        cc += '{:02x}'.format(c[n][0])
        cc += '{:02x}'.format(c[n][1])
    with open(ciphertext_file,'w') as f:
        f.write(cc)
    print("\nCiphertext HEX: 0x" + cc)
    # print(cipher)
    return cipher

def decrypt():
    print('\nDECRYPTION\n')
    global round_num
    global ws
    global cs
    global key
    global current_used_keys
    temp = []
    #print(cs)
    ws = cs
    for i in range(4):
        w = ws[i]
        k = key[i]
        rs[i] = []
        for j in range(2):
            temp.append(w[j] ^ int(k[j],16))
        rs[i] += temp
        temp.clear()
    round_num = 0
    R0 = rs[0]
    R1 = rs[1]
    R2 = rs[2]
    R3 = rs[3]
    # R0 = cs[0]
    # R1 = cs[1]
    # R2 = cs[2]
    # R3 = cs[3]

    rr0 = None
    rr1 = None
    rr2 = None
    rr3 = None
    round = 19
    for _ in range(20):
        print('\nBeginning of Round: {}'.format(round))
        F0, F1 = F_decrypt(R0, R1, round)
        PREV_R0 = R0
        PREV_R1 = R1
        # print('r0')
        # print(R0)
        R0 = int('{:02x}{:02x}'.format(R2[0],R2[1]),16) ^ F0 # next R0
        R1 = int('{:02x}{:02x}'.format(R3[0],R3[1]),16) ^ F1 # next R1
        R2 = [int('{:04x}'.format(R0)[0:2],16), int('{:04x}'.format(R0)[2:4],16)]
        R3 = [int('{:04x}'.format(R1)[0:2],16), int('{:04x}'.format(R1)[2:4],16)]
        R0 = R2
        R1 = R3
        print('Subkeys used:', end=" ")
        y = ''
        [print("0x{} ".format(x),end=" ") for x in current_used_keys[round]]
        y0 = R2
        y1 = R3
        y2 = PREV_R0
        y3 = PREV_R1

        rr0 = y2
        rr1 = y3
        rr2 = y0
        rr3 = y1

        R2 = PREV_R0
        R3 = PREV_R1
        cipher = '{:02x}{:02x}'.format(y0[0],y0[1]) + '{:02x}{:02x}'.format(y1[0],y1[1]) + '{:02x}{:02x}'.format(y2[0],y2[1]) + '{:x}{:x}'.format(y3[0],y3[1])
        print('\nBlock: 0x{}'.format(cipher))
        print('End of Round: {}'.format(round))
        round -= 1

    yy0 = rr0
    yy1 = rr1
    yy2 = rr2
    yy3 = rr3
    cipher = '{:02x}{:02x}'.format(yy0[0],yy0[1]) + '{:02x}{:02x}'.format(yy1[0],yy1[1]) + '{:02x}{:02x}'.format(yy2[0],yy2[1]) + '{:x}{:x}'.format(yy3[0],yy3[1])
    temp = []
    c = {}
    m = 4
    idx = 0
    for i in range(0,16,4):
        w = cipher[i:(i+4)]
        k = key[(i-m)%4]
        m-=1
        c[idx] = []
        id = 0
        for j in range(0,4,2):
            temp.append(int(w[j:(j+2)],16) ^ int(k[id],16))
            id+=1
        c[idx] += temp
        idx+=1
        temp.clear()
    cc = ''
    h = ''
    for n in range(4):
        h += '{:02x}'.format(c[n][0])
        h += '{:02x}'.format(c[n][1])
        cc += chr(int('{:02x}'.format(c[n][0]),16))
        cc += chr(int('{:02x}'.format(c[n][1]),16))
    print("\nPlaintext HEX: 0x" + h)
    print("\nPlaintext ASCII: " + cc)
    return cipher

def F(R0, R1, round):
    T0 = G(R0, round)
    T1 = G(R1, round)
    F0 = (int(T0,16) + 2*int(T1,16) +  int(K(4*round)+K(4*round+1), 16)) % 2**16
    F1 = (2*int(T0,16)+int(T1,16) + int(K(4*round+2)+K(4*round+3), 16)) % 2**16

    print('t0: {} t1: {}'.format(T0,T1))
    print('f0: {} f1: {}'.format(hex(F0),hex(F1)))
    return F0, F1

def F_decrypt(R0, R1, round):
    T0 = G_decrypt(R0, round, 0)
    T1 = G_decrypt(R1, round, 4)
    F0 = (int(T0,16) + 2*int(T1,16) +  int(K_decrypt(round,8)+K_decrypt(round,9), 16)) % 2**16
    F1 = (2*int(T0,16)+int(T1,16) + int(K_decrypt(round,10)+K_decrypt(round,11), 16)) % 2**16

    print('t0: {} t1: {}'.format(T0,T1))
    print('f0: {} f1: {}'.format(hex(F0),hex(F1)))
    return F0, F1

def G(w, round):
    g1 = w[0]
    g2 = w[1]

    # g3
    de = int(K(4*round),16)
    idx = hex(g2 ^ int(de))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g3 = ftable[x][y] ^ g1

    # g4
    idx = hex(g3 ^ int(K(4*round+1),16))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g4 = ftable[x][y] ^ g2

    # g5
    idx = hex(g4 ^ int(K(4*round+2),16))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g5 = ftable[x][y] ^ g3

    # g6
    idx = hex(g5 ^ int(K(4*round+3),16))
    #print(idx)
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g6 = ftable[x][y] ^ g4
    print("g1: {:02x} g2: {:02x} g3: {:02x} g4: {:02x} g5: {:02x} g6: {:02x}".format(g1,g2,g3,g4,g5,g6))
    return '{:02x}{:02x}'.format(g5,g6)

def G_decrypt(w, round, v):
    g1 = w[0]
    g2 = w[1]

    # g3
    de = int(K_decrypt(round, v),16)
    idx = hex(g2 ^ de)
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g3 = ftable[x][y] ^ g1

    # g4
    idx = hex(g3 ^ int(K_decrypt(round, 1+v),16))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g4 = ftable[x][y] ^ g2

    # g5
    idx = hex(g4 ^ int(K_decrypt(round, 2+v),16))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g5 = ftable[x][y] ^ g3

    # g6
    idx = hex(g5 ^ int(K_decrypt(round, 3+v),16))
    x = int(idx[-2:-1],16) if len(idx) == 4 else 0
    y = int(idx[-1:],16)
    g6 = ftable[x][y] ^ g4
    print("g1: {:02x} g2: {:02x} g3: {:02x} g4: {:02x} g5: {:02x} g6: {:02x}".format(g1,g2,g3,g4,g5,g6))
    return '{:02x}{:02x}'.format(g5,g6)

def generate_subkeys():
    global new_key
    global key
    global key_str

    result = leftRotate(int(key_str,16),1)
    kk = '{0:x}'.format(int(bin(result)[-80:],2))
    keys.append(kk)
    j = 1
    for i in range(1,240):
        j = 1
        result = leftRotate(int(keys[i-1],16),1)
        ss = '{0:b}'.format(result)
        ss = ss[-80:]
        s2 = ss
        if(len(ss)<80):
            n = len(ss)
            for _ in range(n,80):
                s2 = '0'+s2
        else:
            s2 = ss
        ss = s2
        kk = '{0:x}'.format(int(ss,2))
        s3 = kk
        if(len(s3)<20):
            n = len(s3)
            for _ in range(n,20):
                s3 = '0'+s3
        else:
            s3 = s3
        keys.append(s3)
    # for v in range(len(keys)):
    #     print(keys[v])

# https://stackoverflow.com/questions/46202913/python-cut-a-x-bit-binary-number-to-a-byte-8bit/46202957
def K(x):
    global new_key
    global key_str
    global current_used_keys
    global round_num
    z = x % 10
    a = z*2
    str = keys[new_key]
    new_key += 1
    if(int(z) == 0):
        #print("K: " + str[-(a+2):])
        current_used_keys[round_num].append(str[-(a+2):])
        return str[-(a+2):]
    else:
        #print("K: " + str[-(a+2):-a])
        current_used_keys[round_num].append(str[-(a+2):-a])
        return str[-(a+2):-a]

def K_decrypt(r, z):
    global current_used_keys
    return current_used_keys[r][z]


def main():
    global plaintext_file
    global key_file
    global cs
    global current_used_keys
    global ciphertext_file
    if (len(sys.argv) != 4):
        print()
        print("error: incorrect number of arguments -> {}\n".format(len(sys.argv)))
        print("usage: [python | python3] PSU-CRYPT.py <plaintext.txt> <key.txt> <ciphertextt.txt>")
        exit(1)
    else:
        plaintext_file = sys.argv[1]
        key_file = sys.argv[2]
        ciphertext_file = sys.argv[3]
#        print_input_file_names()
    generate_subkeys()
    read_plaintext(plaintext_file)
    read_hex_to_key(key_file)
    encrypt_0()
    read_ciphertext()
    decrypt()

if __name__ == '__main__':
    main()
