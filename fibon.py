#0 1 1 2 3 5 8 13 21
def input_int (prompt, err = "Введено не число"):
    isNumber = False
    while not isNumber:
        a = input (prompt)
        try:
            a = int(a)
            isNumber = True
        except:
            print (err)
    return a
a = input_int ("Введите число ")
x, y = [0, 1]
while a > x:
    z = x + y
    #print (z)
    x, y = [y, z]
if a == x:
    print ("Число Фибоначчи")
else:
    print ("Не число Фибоначчи")