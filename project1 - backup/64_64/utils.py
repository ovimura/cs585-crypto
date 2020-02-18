INT_BITS = 8

# Function to left
# rotate n by d bits
def leftRotate(n, d):
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (INT_BITS - d))

print(leftRotate(1,3))


def read_ascii_to_hex():
    with open('key.txt') as f:
            data = f.read()

    s = "".join("{:02x}".format(ord(c)) for c in data[:-1])
    return s

#print(read_ascii_to_hex())
def pr():
    h = "4142414241424142"

    li = []
    for i in range(0,len(h),2):
        li.append(h[i:i+2])
    print(li)

def read_hex_to_hex():
    with open('key.txt') as f:
            data = f.read()
    d = data[:-1]
    li = []
    for i in range(0,len(d),2):
        li.append(d[i:i+2])
    print(li)
    return li

read_hex_to_hex()



print('numm')
print(hex(leftRotate(int(0x4142414241424142),1)))
print("{:b}".format(int(0x4142414241424142)))
res = leftRotate(int('4142414241424142',16),1)
print(res)
s1 = "{:b}".format(int(0x4142414241424142))
s = "{:b}".format(int(bin(res),2))

# fill 64 bits
if(len(s1)<64):
    n = len(s1)
    for _ in range(n,64):
        s1 = '0'+s1

print(s[-64:])
print(s1)
print(s1)
print("{:b}".format(int(bin(res),2)))
print('{0:x}'.format(int(bin(res),2)))
print('-----')

gg = leftRotate(3132393435363733,1)
print(gg)
print(''.join(format(gg, 'x'))) # for y in gg))
