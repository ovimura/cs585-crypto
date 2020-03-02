# CS585: Project 2
# Student: Ovidiu Mura
# Due: March 4, 2020

import random

p = 0
g = 2
e = 0
d = 0

N = 0

pub_key = 'pubkey.txt'
pri_key = 'prikey.txt'
seed = ""

plaintext_file = "ptext.txt"
ciphertext_file = "ctext.txt"
decrypted_ciphertext_file = "dtext.txt"


def exponentiation_modulo(b, e):
    """
    It perform exponentiation and apply modulo N for each multiplication step.
    Reference: https://www.geeksforgeeks.org/exponential-squaring-fast-modulo-multiplication/
    :param b: base
    :param e: exponent
    :return: result
    """
    global N
    t = 1
    while(e > 0):
        if (e % 2 != 0):
            t = (t * b) % N
        b = (b * b) % N
        e = int(e / 2)
    return t % N

def power(x, y, p):
    """
    Utility function to do modular exponention.
    :param x: base
    :param y: exponent
    :param p: modulo
    :return:
    """
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y>>1
        x = (x * x) % p
    return res


def millerTest(d, n):
    """
     This function is called
     for all k trials. It returns
     false if n is composite and
     returns true if n is probably prime.
     Reference: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin
    :param d: odd number such that d*2^r = n-1
    :param n:
    :return: True if n is probably prime, and False if n is composite
    """
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def isPrime( n, k):
    """
     It returns false if n is
     composite and returns true if n
     is probably prime.
    :param n: the integer to be tested
    :param k: accuracy level, higher value of k more accuracy
    :return: True if the integer is prime, False otherwise.
    """
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(k):
        if millerTest(d, n) == False:
            return False
    return True

def gcd(a, b):
    """
    It calculates gcd - greatest common denominator.
    :param a: first integer
    :param b: second integer
    :return: gcd result
    """
    while b:
        a, b = b, a % b
    return a

def setup():
    """
    It setup the values for public key and private key.
    :return:
    """
    global g
    global e
    global p
    global d
    global seed
    global N
    while True:
        r = random.randint(178956970, 357913940)
        q = r*12 + 5
        while isPrime(q,15) is False:
            r = random.randint(178956970, 357913940)
            q = r*12 + 5
        p = 2*q + 1
        if isPrime(p,15) is True:
            break
    print("p: {}, q: {}".format(p,q))

    for _ in range(1,p):
        y = random.randint(1,p-1)
        x = gcd(y, p)
        if x == 1:
            d = y
            break
    N = p
    e = exponentiation_modulo(2, d)
    t1 = "{} {} {}".format(p, g, e)
    t2 = "{} {} {}".format(p, g, d)
    tx1 = "p:{}, g:{}, e:{}".format(p, g, e)
    tx2 = "p:{}, g:{}, d:{}".format(p, g, d)
    print(tx1)
    print(tx2)
    with open(pub_key, "w+") as f1:
        f1.write(t1)
    with open(pri_key, "w+") as f2:
        f2.write(t2)

def read_keys():
    """
    It reads the keys from the files.
    :return:
    """
    global pub_key, pri_key
    global p, g, d, e, N
    with open(pri_key) as f:
        data = f.read()
    data = data.split(" ")
    p = int(data[0])
    g = int(data[1])
    d = int(data[2])
    print(p)
    print(g)
    print(d)
    with open(pub_key) as f:
        data = f.read()
    data = data.split(" ")
    e = int(data[2])
    print(e)
    N = p

def encryption():
    """
    It encrypts the plaintext from ptext.txt file with the public key from pubkey.txt file.
    :return:
    """
    global p, g, d, e, N
    global plaintext_file, ciphertext_file
    dbits = {}
    blocks = {}
    with open(plaintext_file, "r") as f:
        data = f.read()
    b = ["{0:08b}".format(ord(x)) for x in data[:-1]]
    bits = str(b).replace('[','').replace(']','').replace('\', \'','').replace('0b','').replace('\'','')
    temp = bits
    i = 0
    for x in range(0, len(bits),32):
        dbits[i] = temp[x:x+32]
        i += 1
    print("\nPlaintext in Bytes, 32-bits blocks:")
    print(dbits)
    random.seed(1)
    N = p
    for z in range(len(dbits.keys())):
        k = random.randint(1,10000)
        C1 = exponentiation_modulo(g,k) % p
        C2 = (exponentiation_modulo(e,k)*int(dbits[z],2)) % p
        blocks[z] = [k, C1, C2]
    print("\nCiphertext, key + block pairs: (k, C1, C2):")
    print(blocks)
    cc = ""
    with open(ciphertext_file, 'w+') as f:
        for i in range(len(blocks.keys())):
            cc += "{} {} ".format(blocks[i][1],blocks[i][2])
        f.write(cc)

def decryption():
    """
    It decrypts the ciphertext from the ctext.txt file and stores the plaintext into the dtext.txt file.
    :return:
    """
    global p, g, d, e
    global plaintext_file, ciphertext_file, pri_key, pub_key
    print()
    with open(pri_key, "r") as f:
        data = f.read()
    p = data.split(" ")[0]
    g = data.split(" ")[1]
    d = data.split(" ")[2]
    with open(pub_key, "r") as f:
        data = f.read()
    e = data.split(" ")[2]
    print("p: {}".format(p))
    print("g: {}".format(g))
    print("d: {}".format(d))
    print("e: {}".format(e))
    with open(ciphertext_file, "r") as f:
        data = f.read()
    temp = data[:-1].split(" ")
    ms = []
    for u in range(0, len(temp), 2):
        C1 = data.split(" ")[u]
        C2 = data.split(" ")[u+1]
        c1 = exponentiation_modulo(int(C1),(int(p)-1-int(d))) % int(p)
        c2 = (int(C2) % int(p))
        m = (c1*c2) % int(p)
        ms.append(m)
    print("\nDecrypted blocks: ", end="")
    print(ms)
    txt = ""
    for u in range(len(ms)):
        bys = "{:032b}".format(int(ms[u]))
        for i in range(0,32,8):
            b = bys[i:i+8]
            if(int(b,2) != 0):
                txt += chr(int(b,2))
    print("Decrypted Ciphertext: ", end="")
    print(txt)
    with open(decrypted_ciphertext_file, "w+") as f:
        f.write(txt)


def main():
    global p, g, d, e
    global plaintext_file, ciphertext_file
    global seed
    print("\nChoose one of the following options: ")
    print("     1. - key generation")
    print("     2. - encryption")
    print("     3. - decryption")
    i = input("Enter your value: ")
    while int(i) not in [1,2,3]:
        i = input("Enter one of the options [1,2,3]: ")
    if(int(i) == 1):
        print("\nWelcome to Key Generation!\n")
        seed = input("Enter a random number: ")
        while seed.isnumeric() is not True:
            seed = input("Enter a random number: ")
        random.seed(int(seed))
        setup()
    elif int(i) == 2:
        read_keys()
        encryption()
    elif int(i) == 3:
        read_keys()
        decryption()

if __name__ == "__main__":
    main()
