sInput = input ("Введите текст ")
dict = {}
for a in sInput:
    if a in dict:
        dict [a] += 1
    else:
        dict [a] = 1
while True:
    pInput = input ("Введите букву ")
    if "stop" == pInput:
        break
    if pInput in dict:
        print (dict [pInput])
    else:
        print("Такой буквы нет")