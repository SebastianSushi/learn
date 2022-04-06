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
def fact (x):
    f = 1
    for i in range(2, x + 1, 1):
    #    print (i)
        f = f * i
    return f
def fact_ex (x):
    if x == 1: return 1
    else: return x * fact_ex (x - 1)
a = input_int ("Введите число ")
print (fact_ex(a))
print (fact_ex(3))
print (fact_ex(5))