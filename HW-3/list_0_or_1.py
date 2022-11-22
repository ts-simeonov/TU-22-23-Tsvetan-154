z = int(input('Kolko na broi chisla: '))
l = []

for i in range(z):
    x = int(input('Vuvedete proizvolno chislo: '))
    l.append(x)

y = int(input('Vuvedete 0 ili 1: '))

if y == 0:
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] += 5
    print(l)
elif y == 1:
    for i in range(len(l)):
        if i % 2 == 1:
            l[i] += 10
    print(l)
else:
    print('Vuveli ste chislo razlichno ot 0 i 1, zapochnete ot nachalo')