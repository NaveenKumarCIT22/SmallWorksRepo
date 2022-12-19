"""

This algorithm is going to add all the even fibonacci numbers upto the specified number(inclusive).

"""

while  True:
    hist = {0:0}
    n = input("Enter the number of cases you wish to test: ")
    if n=="nill":
        break
    elif n==0:
        print("Enter valid range please!")
    n = int(n)
    for _ in range(n):
        q = int(input("Enter the test case: "))
        if q in hist.keys():
            print(hist[q])
            continue
        a = 0
        b = 1
        c = 0
        s = 0
        if q>=0:
            while c<=q:
                c = a+b
                a = b
                b = c
                # print(a,end=" ")
                if a%2==0:
                    s += a
            # print(b)
        else:
            while c>=q:
                c = b-a
                b = a
                a = c
                # print(b,end=" ")
                if b%2==0:
                    s += b
            # print(a)
        hist[q] = s
        print(s)
