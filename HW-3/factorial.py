z = int(input('Vuvedete chislo, za da poluchite negoviq faktoriel: '))
f = 1

for i in range(1,z+1):
    f *= i
print(f'Faktorielat na {z} e {f}!')