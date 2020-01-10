
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

split = []

def split_by(ii=0, step=4):
    global split
    global c
    while ii < len(c):
        print(c[ii:ii+step])
        split.append(c[ii:ii+step])
        ii += step

split_by(0,8)
print(len(c))
print(split)

n = 0
print("Step 1: get every n^th letter from group strings, n = {}".format(n))

subkey1 = []
if n > 0:
    for i in range(len(split)-1):
        subkey1.append(split[i][n])
else:
    for i in range(len(split)):
        subkey1.append(split[i][n])

def print_freq_of_letters(subkey1):
    print("{}:{}".format('A',len([x for x in subkey1 if x == 'A'])))
    print("{}:{}".format('B',len([x for x in subkey1 if x == 'B'])))
    print("{}:{}".format('C',len([x for x in subkey1 if x == 'C'])))
    print("{}:{}".format('D',len([x for x in subkey1 if x == 'D'])))
    print("{}:{}".format('E',len([x for x in subkey1 if x == 'E'])))
    print("{}:{}".format('F',len([x for x in subkey1 if x == 'F'])))
    print("{}:{}".format('G',len([x for x in subkey1 if x == 'G'])))
    print("{}:{}".format('H',len([x for x in subkey1 if x == 'H'])))
    print("{}:{}".format('I',len([x for x in subkey1 if x == 'I'])))
    print("{}:{}".format('J',len([x for x in subkey1 if x == 'J'])))
    print("{}:{}".format('K',len([x for x in subkey1 if x == 'K'])))
    print("{}:{}".format('L',len([x for x in subkey1 if x == 'L'])))
    print("{}:{}".format('M',len([x for x in subkey1 if x == 'M'])))
    print("{}:{}".format('N',len([x for x in subkey1 if x == 'N'])))
    print("{}:{}".format('O',len([x for x in subkey1 if x == 'O'])))
    print("{}:{}".format('P',len([x for x in subkey1 if x == 'P'])))
    print("{}:{}".format('Q',len([x for x in subkey1 if x == 'Q'])))
    print("{}:{}".format('R',len([x for x in subkey1 if x == 'R'])))
    print("{}:{}".format('S',len([x for x in subkey1 if x == 'S'])))
    print("{}:{}".format('T',len([x for x in subkey1 if x == 'T'])))
    print("{}:{}".format('U',len([x for x in subkey1 if x == 'U'])))
    print("{}:{}".format('V',len([x for x in subkey1 if x == 'V'])))
    print("{}:{}".format('W',len([x for x in subkey1 if x == 'W'])))
    print("{}:{}".format('X',len([x for x in subkey1 if x == 'X'])))
    print("{}:{}".format('Y',len([x for x in subkey1 if x == 'Y'])))
    print("{}:{}".format('Z',len([x for x in subkey1 if x == 'Z'])))

print_freq_of_letters(subkey1)

print("Step 2: Frequency Analysis")
print("decrypt this string 26 times, once for each of the 26 possible subkeys")
subkeys = []
s = ""
for j in range(len(subkey1)):
    s+= subkey1[j]

#print(s)
subkeys.append(s)
subkey = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for k in range(26):
    s = ""
    for j in range(len(subkey1)):
        a = ord(subkey1[j])-k
        if a < 65:
            a += 26
        if a > 90:
            a -= 26
        s += chr(a)
        subkey[k].append(chr(a))
    print(s)
    subkeys.append(s)

alphabet = [chr(x) for x in range(65,91)]
print(alphabet)


freqs = []

for i in range(26):
    f = []
    for y in alphabet:
        f.append((y,len([x for x in subkey[i] if x == y])))
    freqs.append(f)

def subkey1():
    print("{}:{}".format('A',len([x for x in subkey[1] if x == 'A'])))
    print("{}:{}".format('B',len([x for x in subkey[1] if x == 'B'])))
    print("{}:{}".format('C',len([x for x in subkey[1] if x == 'C'])))
    print("{}:{}".format('D',len([x for x in subkey[1] if x == 'D'])))
    print("{}:{}".format('E',len([x for x in subkey[1] if x == 'E'])))
    print("{}:{}".format('F',len([x for x in subkey[1] if x == 'F'])))
    print("{}:{}".format('G',len([x for x in subkey[1] if x == 'G'])))
    print("{}:{}".format('H',len([x for x in subkey[1] if x == 'H'])))
    print("{}:{}".format('I',len([x for x in subkey[1] if x == 'I'])))
    print("{}:{}".format('J',len([x for x in subkey[1] if x == 'J'])))
    print("{}:{}".format('K',len([x for x in subkey[1] if x == 'K'])))
    print("{}:{}".format('L',len([x for x in subkey[1] if x == 'L'])))
    print("{}:{}".format('M',len([x for x in subkey[1] if x == 'M'])))
    print("{}:{}".format('N',len([x for x in subkey[1] if x == 'N'])))
    print("{}:{}".format('O',len([x for x in subkey[1] if x == 'O'])))
    print("{}:{}".format('P',len([x for x in subkey[1] if x == 'P'])))
    print("{}:{}".format('Q',len([x for x in subkey[1] if x == 'Q'])))
    print("{}:{}".format('R',len([x for x in subkey[1] if x == 'R'])))
    print("{}:{}".format('S',len([x for x in subkey[1] if x == 'S'])))
    print("{}:{}".format('T',len([x for x in subkey[1] if x == 'T'])))
    print("{}:{}".format('U',len([x for x in subkey[1] if x == 'U'])))
    print("{}:{}".format('V',len([x for x in subkey[1] if x == 'V'])))
    print("{}:{}".format('W',len([x for x in subkey[1] if x == 'W'])))
    print("{}:{}".format('X',len([x for x in subkey[1] if x == 'X'])))
    print("{}:{}".format('Y',len([x for x in subkey[1] if x == 'Y'])))
    print("{}:{}".format('Z',len([x for x in subkey[1] if x == 'Z'])))

for i in range(len(freqs)):
    print(freqs[i])

def getKey(item):
    return item[1]

eng = ['E', 'T', 'A', 'O', 'I', 'N']

print("Step 3: find out their most likely subkey")
print("English Frequency Match Score: ")
score = []
for i in range(len(freqs)):
    #print("{}".format(chr(65+i)))
    aa = [Z for Z in [x[0] for x in sorted(freqs[i], key=getKey, reverse=True)[:6]] if Z in eng]
    #print(aa)
    print("{}:{}".format(chr(65+i), len(aa)))
    score.append((chr(65+i), len(aa)))
    #print(sorted(freqs[i], key=getKey, reverse=True)[:6])

print("Most Likely Subkey:")
print(sorted(score, key=getKey, reverse=True)[0])
