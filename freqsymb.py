#input string from keyboard
sInput = input ("Введите слово ")
#empty dict for chars calculation
dict = {}
#calculate
for a in sInput:
    if a in dict:
        dict [a] += 1
    else:
        dict [a] = 1
#sort keys by chars count
sortedKeys = sorted(dict, key=dict.get, reverse=True)
#fill resul dictionary with right sort
rDict = {}
for a in sortedKeys: rDict[a] = dict[a]
#printing result
print (rDict)