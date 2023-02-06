#Ler um número e dizer se é primo
n = int(input('Digite um número e vou dizer se é primo: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('')
print('o número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('é primo')
else:
    print('não é primo')
