
c = "QSWWFCEBWREILVMCJVCHJWFUSVGUMQKSKSTUJSXRULAJYQLFSXCHPUHKWRVYMMGAJIGJZMKRZSWAYAHKWQCFZKBMMWEIUMVYFEENLIEJQLKXVQGQAHGIKPXPTIPCXVLMXXYUIMTLVFGJIWZPSQOYUBHHMQRILBPFWRAILIKCFSVYOXXALMPAZBAYUOGLJIKCARELVILGFKNSLABLYXJCJBXAZRKKLMDLGAPUJAMCYEPIXZTNZCVIKZBACMPNVZGCLYUYIATLVWOOXOECEENCTQHSKTCSCWTBKTCMKAXAMVKNPAVYFRGLJIGBXMTYNIEJKYPFZSXAJCRNFOKYHLAQYQVFOSTEJBHMTWEOIMVMFXGHKAHGLGCHKJXSFHGLJBHMVWVYXIGMYVCJYGLEGENCJBHFAHGNYMYYUXVBRBVMFXGHKMQGKXUUKIEJTCGGSMWBARICKQGQGQGNYQGEWPUYRVWQAREYJBXESRQAIIIFQMUUTWGAWTVHFBTQHIECWQVKWXJIUWYADEPXVAMGFIFUKIWCDMXYIGBRUEPVVCLCVMPUCTLMJXUIWQGEWRKILATLVAQLIGBLYEVNRKDQKXGARVHEJERBPQLYFEPWZMGRHVCWKQVCOLGHJXBCKMPNYMKCNSNOKQHLSVAQRZPPGXGCEQGTAWKVCMBLCSTQYMGBSZKHTQXKTIFXVLLCUVGNDMTLARICEIIYARVCEOMFSXYUJAMCYEPIXZTNZCVBZAPMJOUCEBACVMICKIEUGVNXKWHUZITYRNBJWPKEVIGGEEIYTIGZWWVYRTMFAPAYEKHBWHYCKPBLXSTGRBBMFJQLVFTKHPGJZFXJNENOVAUPAKJNEMLQSRFZZTMCJWGNKQGEKJQLRVBKSKGUIMGMJQCFCGVFSRIYUBHYXJGWKBACAQCAVATCKXJYKQVJGSMVLBAYUOGLJKTLSPUIDIGGHYNUKMMFWQDUJMWMFEUYTZXRUSFYNQMFFSTYXIKBXSTBFEMFWMPJLBLKSOGNYMBKSKGFFWDTAWWUCTRRZMUNVKALAUWYTIGZWYUYUNHPWXJCTIEPWEUIEALSULCMKWXTSHGWVVLMJWJCGWKCEFGXDMLQSKGMZVYYUIDIFSIFGXQMSCMRZIUYDMMFGHUWRVTJKSDYLAXBFIHUIQHSKPAZFZLCUYTCKGWCXIPXVZLRZISOVAMGGRKMYWPRGXGFCBACVMHZVZXLUIDYKEXCFEPCDIZCLLCNJJXCFQQXZNBCVJQLCMZGLMOUKMKCSWQHJIGBGRGNYIMQTIGHTPTLYIFNFAXAJIVFPKHLLEKHDIEGUMQOJQGDGVOUKQHLXVQGNQKCVQCARHBLW"

def freq_cipher():
    global c
    cipher = sorted(list(c))
    print("{}:{}".format('A',len([x for x in cipher if x == 'A'])))
    print("{}:{}".format('B',len([x for x in cipher if x == 'B'])))
    print("{}:{}".format('C',len([x for x in cipher if x == 'C'])))
    print("{}:{}".format('D',len([x for x in cipher if x == 'D'])))
    print("{}:{}".format('E',len([x for x in cipher if x == 'E'])))
    print("{}:{}".format('F',len([x for x in cipher if x == 'F'])))
    print("{}:{}".format('G',len([x for x in cipher if x == 'G'])))
    print("{}:{}".format('H',len([x for x in cipher if x == 'H'])))
    print("{}:{}".format('I',len([x for x in cipher if x == 'I'])))
    print("{}:{}".format('J',len([x for x in cipher if x == 'J'])))
    print("{}:{}".format('K',len([x for x in cipher if x == 'K'])))
    print("{}:{}".format('L',len([x for x in cipher if x == 'L'])))
    print("{}:{}".format('M',len([x for x in cipher if x == 'M'])))
    print("{}:{}".format('N',len([x for x in cipher if x == 'N'])))
    print("{}:{}".format('O',len([x for x in cipher if x == 'O'])))
    print("{}:{}".format('P',len([x for x in cipher if x == 'P'])))
    print("{}:{}".format('Q',len([x for x in cipher if x == 'Q'])))
    print("{}:{}".format('R',len([x for x in cipher if x == 'R'])))
    print("{}:{}".format('S',len([x for x in cipher if x == 'S'])))
    print("{}:{}".format('T',len([x for x in cipher if x == 'T'])))
    print("{}:{}".format('U',len([x for x in cipher if x == 'U'])))
    print("{}:{}".format('V',len([x for x in cipher if x == 'V'])))
    print("{}:{}".format('W',len([x for x in cipher if x == 'W'])))
    print("{}:{}".format('X',len([x for x in cipher if x == 'X'])))
    print("{}:{}".format('Y',len([x for x in cipher if x == 'Y'])))
    print("{}:{}".format('Z',len([x for x in cipher if x == 'Z'])))

def split_by(ii=0, step=4):
    global c
    while ii < len(c):
        print(c[ii:ii+step])
        ii += step

import re
d = {}
def find_repeating_patern(length=3):
    global c
    global d
    counts = {}
    i = 0
    while i < len(c) and len(c[i:i+length]) == length:
        print(c[i:i+length])
        a = 0
        counts[c[i:i+length]] = []
        for m in re.finditer(c[i:i+length],c):
            if a != 0:
                a = m.start() - a + length
            if(a != 0):
                counts[c[i:i+length]].append(a)
            print("found ", m.start(), m.end(), " between {}".format(a))
            a = m.end()
        i += length
    print(counts)
    d = counts

find_repeating_patern(3)

fre = []
for k in d.keys():
    fre.append((k,len(d[k])))
print(fre)

print(max([x[1] for x in fre]))
#kk = [x for x in fre if x[1] == max([x[1] for x in fre])]
kk = [x for x in fre]
# kk1 = [x for x in fre if x[1] == max([x[1] for x in fre])]
print(kk)


for i in range(len(kk)):
    if len(d[kk[i][0]]) != 0:
        print(d[kk[i][0]])
#import math
#print(math.gcd(d[kk[0][0]][0],d[kk[0][0]][1]))
