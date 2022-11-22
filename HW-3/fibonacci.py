z = int(input('Purvite kolko n+2 chisla iskate?'))

a = 0
b = 1
c = 0

for i in range(z+2):
    print(a)
    c = a + b
    a = b
    b = c
    i += 1