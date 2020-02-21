import random

p = 0
g = 2
e = 0

pub_key = 'pubkey.txt'
pri_key = 'prikey.txt'
seed = ""

_33bit = 8589934591

def main():
    global g
    global seed
    # random.seed(ii)
    # print(random.randint(1,ii))
    # print(random.randint(1,ii))
    # print(random.randint(1,ii))
    # exit(9)
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
        print(seed.isnumeric())
        while seed.isnumeric() is not True:
            seed = input("Enter a random number: ")
        print(seed.isnumeric())
        random.seed(int(seed))
    #print(random.randint(‭2147483648‬, 4294967295))
    # max 32 bits: 4294967295
    # min 32 bits: 2147483648
    r = random.randint(178956970, 357913940)
    q = r*12 + 5
    print(q)
    exit(4)

if __name__ == "__main__":
    main()
