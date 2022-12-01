z = int(input('Колко двойки стойности: '))
d = dict()
l = list()

for i in range(z):
    k = input('Въведете ключ: ')
    v = input('Въведете стойност: ')
    d[k] = v

y = int(input('Колко стойности да се запазят: '))

for i in range(y):
    q = input('Въведете стойност: ')
    l.append(q)

for i in range(len(l)):
    if l[i] in d.keys():
        x = l[i]
        l[i] = d[l[i]]
        d.pop(x)

print(d)
print(l)