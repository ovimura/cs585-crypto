# CS585: Cryptography
# Student: Ovidiu Mura
# Assignment: Project 1
# Date: Jan 20, 2020

import sys
import binascii

plaintext_file = None
key_file = None

bit_bock_size = 64
bit_key_size = 64

round_num = 0

ws = {}
key = {}
rs = {}
keys = []

ddd = None

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


def print_input_file_names():
    print("plaintext file name: {}".format(plaintext_file))
    print("key file name: {}".format(key_file))

def read_plaintext(file, size):
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
    print('words')
    print(ws)
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

def read_hex_to_key(file='key.txt'):
    global key
    with open(file) as f:
            data = f.read()
    d = data[:-1]
    li = []
    for i in range(0,len(d),2):
        li.append(d[i:i+2])
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

    print(d)
    return d

print(read_hex_to_key())

def encrypt():
    global round_num
    global ws
    global key
    temp = []
    for i in range(4):
        w = ws[i]
        k = key[i]
        rs[i] = []
        for j in range(2):
            temp.append(w[j] ^ k[j])
        rs[i] += temp
        temp.clear()
    print('rounds')
    print(rs)
    T0 = G(rs[0], round_num)
    T1 = G(rs[1], round_num)

def F(R1, R2, round):
    global rs
    F0, F1 = 0
    #R0
    return F0, F1

def G(r, round):
    pass


# https://stackoverflow.com/questions/46202913/python-cut-a-x-bit-binary-number-to-a-byte-8bit/46202957
def K(x):
    global key
    print(key)
    n = ''.join(format(ord(xx), 'x') for xx in x)
    print('n')
    print(n)
    z = int('0x'+'5',16)
    print(z)
    r = leftRotate(z,1)
    # print(bin(r)[-3:]) # the same thing like the following statement
    print("{:b}".format(int(bin(r)[-3:],2)))
    print(r)
    print(''.join(format(z, 'b')))

INT_BITS = 3

# Function to left
# rotate n by d bits
def leftRotate(n, d):
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (INT_BITS - d))

print('numm')
print(leftRotate(3132393435363733,3))
print(leftRotate(int('3132393435363733',10),3))

print('-----')

gg = leftRotate(3132393435363733,1)
print(gg)
print(''.join(format(gg, 'x'))) # for y in gg))


def main():
    global plaintext_file
    global key_file
    global ddd
    if (len(sys.argv) != 3):
        print()
        print("error: incorrect number of arguments -> {}\n".format(len(sys.argv)))
        print("usage: [python | python3] PSU-CRYPT.py <plaintext.txt> <key.txt>")
        exit(1)
    else:
        plaintext_file = sys.argv[1]
        key_file = sys.argv[2]
#        print_input_file_names()

    #read_plaintext(plaintext_file, 10)
    str_key = read_hex_to_key(key_file)
    ddd = str_key
    print('ddd')
    print(ddd)
    #encrypt()
    K(str_key)



if __name__ == '__main__':
    main()
