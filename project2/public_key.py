import random

p = 0
g = 2
e = 0
d = 0

pub_key = 'pubkey.txt'
pri_key = 'prikey.txt'
seed = ""

plaintext_file = "ptext.txt"
ciphertext_file = "ctext.txt"
decrypted_ciphertext_file = "dtext.txt"

def exp_func(x, y):
    exp = bin(y)
    value = x

    for i in range(3, len(exp)):
        value = value * value
        if(exp[i:i+1]=='1'):
            value = value*x
    return value

# print(exp_func(2,4810291259))
# exit(3)

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):

    # Initialize result
    res = 1

    # Update x if it is more than or
    # equal to p
    x = x % p
    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y>>1 # y = y/2
        x = (x * x) % p

    return res

# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n
    x = power(a, d, n)

    if (x == 1 or x == n - 1):
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    # Return composite
    return False

# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime( n, k):

    # Corner cases
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    # Iterate given nber of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False

    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def setup():
    global g
    global e
    global p
    global d
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
    while True:
        r = random.randint(178956970, 357913940)
        q = r*12 + 5
        while isPrime(q,15) is False:
            r = random.randint(178956970, 357913940)
            q = r*12 + 5
        p = 2*q + 1
        if isPrime(p,15) is True:
            break
    for _ in range(1,p-1):
        y = random.randint(1,p-2)
        x = gcd(y, p)
        if x == 1:
            d = y
            break
    #e = 2**d % p
    e = exp_func(2,d) % p
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

def encryption():
    global p, g, d, e
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
    print(dbits)
    # k = random.randint(0,p-1)
    for z in range(len(dbits.keys())):
        k = random.randint(1,10000)
        print("k: {}".format(k))
        #C1 = g**k % p
        #C2 = ((e**k)*int(dbits[z],2)) % p
        C1 = exp_func(g,k) % p
        C2 = (exp_func(e,k)*int(dbits[z],2)) % p
        blocks[z] = [k, C1, C2]

    print(blocks)
    cc = ""
    with open(ciphertext_file, 'w+') as f:
        for i in range(len(blocks.keys())):
            cc += "{} {} ".format(blocks[i][1],blocks[i][2])
        f.write(cc)

def decryption():
    global p, g, d, e
    global plaintext_file, ciphertext_file, pri_key, pub_key
    print('decryption')
    with open(pri_key, "r") as f:
        data = f.read()
    p = data[:-1].split(" ")[0]
    g = data[:-1].split(" ")[1]
    d = data[:-1].split(" ")[2]
    with open(pub_key, "r") as f:
        data = f.read()
    e = data[:-1].split(" ")[2]
    print(p)
    print(g)
    print(d)
    print(e)
    with open(ciphertext_file, "r") as f:
        data = f.read()
    C1 = data[:-1].split(" ")[0]
    C2 = data[:-1].split(" ")[1]
    # c1 = ((int(C1)**(int(p)-1-int(d))) % int(p))
    # c2 = (int(C2) % int(p))
    c1 = exp_func(int(C1),(int(p)-1-int(d))) % int(p)
    c2 = (int(C2) % int(p))
    m = (c1*c2) % int(p)
    print(m)

def main():
    global p, g, d, e
    global plaintext_file, ciphertext_file
    # with open(plaintext_file, 'r') as f:
    #     rr = f.read()
    # print(len(rr))
    # exit(3)
    setup()
    encryption()
    decryption()

if __name__ == "__main__":
    main()
