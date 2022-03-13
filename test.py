isNumber = False
while not isNumber:
    a = input ("age?")
    try:
        a = int(a)
        isNumber = True
    except:
        print ("Введено не число")
if 35 == a:
    print ("Попал в диапазон")
else:
    print ("Не попал в диапазон")