import random

p = 0
g = 0
e2 = 0

pub_key = 'pubkey.txt'
pri_key = 'prikey.txt'

ii =18446744073709551615
#ii += 1

def main():
    global g
    global ii
    random.seed(ii)
    print(random.randint(1,ii))
    print(random.randint(1,ii))
    print(random.randint(1,ii))
    exit(9)
    print("\nChoose one of the following options: ")
    print("     1. - key generation")
    print("     2. - encryption")
    print("     3. - decryption")
    i = input("Enter your value: ")
    while int(i) not in [1,2,3]:
        i = input("Enter one of the options [1,2,3]: ")
    if(int(i) == 1):
        print("Welcome to Key Generation!\n")
        g = input("Enter a random number: ")
    print(i)

if __name__ == "__main__":
    main()
