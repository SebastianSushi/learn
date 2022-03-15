sInput = input ("Введите слово ")
dict = {}
for a in sInput:
    if a in dict:
        dict [a] += 1
    else:
        dict [a] = 1
        Sorted = sorted (dict.items())
print (Sorted)