# CS585: Cryptography
# Student: Ovidiu Mura
# Assignment: Project 1
# Date: Jan 20, 2020

import sys

plaintext_file = None
key_file = None

bit_bock_size = 64
bit_key_size = 64


def print_input_file_names():
    print("plaintext file name: {}".format(plaintext_file))
    print("key file name: {}".format(key_file))

def read_bytes(file, size):
    with open(file) as f:
        data = f.read()
    s = "".join("0x{:02x} ".format(ord(c)) for c in data)
    d = data.encode()
    #print(s.encode()[1])
    print(d[1] ^ 0xFF)
    return s




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

    read_bytes(plaintext_file, 10)




if __name__ == '__main__':
    main()
