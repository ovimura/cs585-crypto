import random

p = 0
g = 2
e = 0

d = 0

pub_key = 'pubkey.txt'
pri_key = 'prikey.txt'
seed = ""

_33bit = 8589934591

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

def main():
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
        print("Welcome to Key Generation!\n")
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
    print()
    print(p)
    for _ in range(1,p-1):
        y = random.randint(1,p-2)
        x = gcd(y, p)
        if x == 1:
            d = y
            break
    print('d',end='\n')
    print(d)
    e = 2**d % p
    print(e)

if __name__ == "__main__":
    main()
