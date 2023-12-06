#ler o primeiro termo e a razão da progressão aritmética e mostrar os 10 primeiros termos
n = int(input('Qual será o primeiro número? '))
r = int(input('e a razão pra progressão?  '))
soma = r * 11
for c in range(n, soma, r):
    print(n, end= '->')
    n = n + r
print('fim')