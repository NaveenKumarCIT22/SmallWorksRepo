rmnltrs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, '0':0}

while True:
    num = 0
    inp = input("Enter a roman numeral: ")
    inp = inp.upper()[::-1]
    inpt = inp+"0"
    inptl = list(inpt)
    if inp=="q":
        break
    for i in range(len(inptl)):
        j = i+1
        try:
            if rmnltrs[inptl[i]] > rmnltrs[inptl[j]]:
                num += rmnltrs[inptl[i]]-rmnltrs[inptl[j]]
                del inptl[j]
            else:
                num += rmnltrs[inptl[i]]
        except Exception as e:
            pass

    print(num)