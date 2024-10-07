#uhloha 6
def fun1(a):
    cifra = 0
    while a>0:
        pc = a % 10
        cifra += 1
        a = a // 10
    return cifra

def fun2(a):
    cifra = fun1(a)
    b = 0
    if cifra % 2 == 0:
        stredne1 = a % (10**(cifra//2))
        while stredne1 > 10:
            stredne1 = stredne1 // 10
        stredne2 = a // (10**(cifra//2))
        while stredne2 > 10:
            stredne2 = stredne2 % 10
        b = stredne1 + stredne2
        print(b)
    else:
        cif = cifra /2+0.5
        stredna3 = a % (10**cif)
        while stredna3 > 10:
            stredna3 = stredna3 // 10
        print(int(stredna3))
print(fun2(123456789))

