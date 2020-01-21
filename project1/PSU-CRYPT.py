# CS585: Cryptography
# Student: Ovidiu Mura
# Assignment: Project 1
# Date: Jan 20, 2020

import sys

plaintext_file = None
key_file = None

bit_bock_size = 64
bit_key_size = 64

round_num = 0

ws = {}
ks = {}

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
    for i in range(0,len(d), 8):
        ws[idx] = []
        x = len(d)%8 if(len(d)<i+x) else 8
        for j in range(i, i+x):
            temp.append(d[j])
        ws[idx] += (temp)
        idx += 1
        temp.clear()
    print(ws)
    return s

def read_key(file):
    global ks
    with open(file) as f:
        data = f.read()
    s = "".join("0x{:02x} ".format(ord(c)) for c in data)
    d = data.encode()[:-1]
    x = 8
    idx = 0
    temp = []
    for i in range(0,len(d), 8):
        ks[idx] = []
        x = len(d)%8 if(len(d)<i+x) else 8
        for j in range(i, i+x):
            temp.append(d[j])
        ks[idx] += (temp)
        idx += 1
        temp.clear()
    print(ks)
    return s


def encrypt():
    global round_num
    global ws
    global ks





def main():
    global plaintext_file
    global key_file

    if (len(sys.argv) != 3):
        print()
        print("error: incorrect number of arguments -> {}\n".format(len(sys.argv)))
        print("usage: [python | python3] PSU-CRYPT.py <plaintext.txt> <key.txt>")
        exit(1)
    else:
        plaintext_file = sys.argv[1]
        key_file = sys.argv[2]
#        print_input_file_names()

    read_plaintext(plaintext_file, 10)
    read_key(key_file)



if __name__ == '__main__':
    main()
