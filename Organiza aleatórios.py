from random import randint
maior = 0
menor = 10
n1 = randint(0,10)
n2 = randint(0,10)
while n2 == n1:
    n2 = randint(0,10)
n3 = randint(0,10)
while n3 == n2 or n3 == n1:
    n3 = randint(0,10)
n4 = randint(0,10)
while n4 == n3 or n4 == n2 or n4 == n1:
    n4 = randint(0,10)
n5 = randint(0,10)
while n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    n5 = randint(0,10)
print(n1, n2, n3, n4, n5)
tupla = (n1, n2, n3, n4, n5)
for c1 in range(0, 5):
    if tupla[c1] < menor:
        menor = tupla[c1]
for c2 in range(0, 5):
    if tupla[c2] > maior:
        maior = tupla[c2]
print(menor, 'menor')
print(maior, 'maior')
