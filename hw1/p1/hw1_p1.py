
def decrypt_1():
    c = "PRYFFZJGCREEZEXFETFDSRKZEXJGRDSPIVHLZIZEXVDRZCKFSVRLKYVEKZTRKVUKYVGIFSCVDKYVPTCRZDZJKYRKKYVIVJEFNRPFWBEFNZEXNYFKYVJVEUVIIVRCCPZJZKJVVDJFSMZFLJKFDVKYRKKYZJNFEKJKFGJGRDRKRCCJGRDDVIJRIVRCIVRUPSIVRBZEXZEKFTFDGLKVIJREUYZARTBZEXCVXZKZDRKVLJVIJVDRZCJPJKVDJJGRDDVIJRIVRCIVRUPJVEUZEXDRZCFLKFWIREUFDTFLEKIZVJREUJKFCVERTTFLEKJYFNVORTKCPNZCCKYZJDRBVKYZEXJSVKKVI"

    for k in range(1,27):
        p = ''
        key = -k
        for i in range(len(c)):
            num = ord(c[i])
            num += key
            if c[i].isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif c[i].islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            p += chr(num)
        print(p)

def decrypt_2():
    c = "PRYFFZJGCREEZEXFETFDSRKZEXJGRDSPIVHLZIZEXVDRZCKFSVRLKYVEKZTRKVUKYVGIFSCVDKYVPTCRZDZJKYRKKYVIVJEFNRPFWBEFNZEXNYFKYVJVEUVIIVRCCPZJZKJVVDJFSMZFLJKFDVKYRKKYZJNFEKJKFGJGRDRKRCCJGRDDVIJRIVRCIVRUPSIVRBZEXZEKFTFDGLKVIJREUYZARTBZEXCVXZKZDRKVLJVIJVDRZCJPJKVDJJGRDDVIJRIVRCIVRUPJVEUZEXDRZCFLKFWIREUFDTFLEKIZVJREUJKFCVERTTFLEKJYFNVORTKCPNZCCKYZJDRBVKYZEXJSVKKVI"

    for k in range(1,26):
        print(k)
        p = ''
        key = -k
        for i in range(len(c)):
            num = ord(c[i])
            num += key
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
            p += chr(num)
        print(p)

decrypt_2()
