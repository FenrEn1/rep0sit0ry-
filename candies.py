a = int(input("Кол-во конфет"))
b = int
c = int

if a <= 5:
    print("Все конфеты в правый корман")
elif a > 5:
    if a % 2 == 0:
        b=a-2
        b=b//2
        c=a+2
        c=c//2
        print( str(b) + " конфет в правом кормане и " + str(c) + " конфет в левом кармане")
    elif a % 2 != 0:
        b=a-5
        b=b//2
        c=a+5
        c=c//2
        print( str(b) + " конфет в правом кормане и " + str(c) + " конфет в левом кармане")
