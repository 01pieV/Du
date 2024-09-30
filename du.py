# uloha 1.
def fun1():
    for i in range(1,11):
        print(i)
fun1()

# uhloha 2.
    # a.)
def fun2(a):
    for i in range(1, a+1):
        print(i)

fun2(5)
    # b.)
def fun2(a):
    for i in range(1, a+1):
        if i < a:
            print(i,end =',')
        else:
            print(i)
fun2(5)

# uloha 3.
def fun3(a):
    for i in range (5, a+1, 2):
        print(i)
fun3(15)

# uloha 4.
def fun4(a):
    for i in range(1, a+1):
        print(i, i**2 )
fun4(9)

# uloha 5.
import math
def fun5(a,b):
    for i in range(a,b+1):
        odmocninca = round(math.sqrt(i), 2)
        print(odmocninca)
fun5(1,6)

#uloha 6.
def fun6(a,b):
    for i in range(a,b+1):
        a = i
        if (a-3) == 0:
            print("x = "  + str(a) +  " funkcia nie je definovana")
        else:
            y = (a ** 2 - 1) / (a - 3)
            print("x = " +str(a) + " y = " + str(y))
fun6(1,20)

#uloha 7.
def fun7(a):
    for i in range(1,a+1):
        if i%3 == 0:
            print(i)
fun7(6)

# uloha 8.
def fun8(a):
    for i in range(1,a+1):
        if i%2 == 0:
            print(i)
fun8(20)

# uloha 9.
def fun9(a,b):
    if a%2 == 0:
        a += 1
    for i in range(a,b+1, 2):
        print(i)
fun9(6, 10)

# uloha 10.
def fun10(b):
    for i in range(0,b):
        c = b-i
        print(c)
fun10(8)

#uloha 11.
def fun11(a):
    for i in range (1, a):
            if i%4 == 0:
                if i%7 == 0:
                    print(i)
fun11(29)

#uloha 12.
def fun12(a):
    celkom = 0
    for i in range(1,a+1):
        celkom += i
    return celkom
print(fun12(5))

#uloha 13.
def fun13(a):
    cel = 0
    for i in range(1,a+1):
        if i%2 == 0:
            cel += i
    print(cel)
fun13(6)

#uloha 14.
def fun14(a,b):
    osem = 0
    for i in range(a,b+1):
        if i % 8 == 0:
            osem +=1
    print(osem)
fun14(5,24)