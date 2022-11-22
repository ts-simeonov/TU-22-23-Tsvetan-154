z = int(input('Vuvedete ednocifreno chislo: '))

y = str(z)
l = []   # Tozi list shte sudurja int-ove
ls = []  # Tozi list shte sudurja string-ove
sum = 0

for i in range(1, z+1):
    x = i * y
    ls.append(x)
    l.append(int(x))

for i in range(0, len(l)):
    sum += l[i]

print(' + '.join(ls), '=', sum)