#ler 3 números e dizer qual é o maior e qual é o menor
print('--+--'*12)
print('  Digite 3 números e vou dizer qual é maior e qual é menor')
print('--+--'*12)
n1 = int(input('1: '))
n2 = int(input('2: '))
n3 = int(input('3: '))
if n1 > n2 > n3:
    print('{} é o maior e {} é o menor'.format(n1, n3))
elif n1 > n3 > n2:
    print('{} é o maior e {} é o menor'.format(n1, n2))
elif n2 > n1 > n3:
    print('{} é o maior e {} é o menor'.format(n2, n3))
elif n2 > n3 > n1:
    print('{} é o maior e {} é o menor'.format(n2, n1))
elif n3 > n1 > n2:
    print('{} é o maior e {} é o menor'.format(n3, n2))
else:
    print('{} é o maior e {} é o menor'.format(n3, n1))