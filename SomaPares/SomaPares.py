#ler 6 números e somar os pares
soma = 0
for c in range (1, 7):
    n = int(input('digite o {} valor: '.format(c)))
    if n %2 == 0:
        soma = n + soma
        print('número par')
    else:
        print('número impar')
print('a soma dos pares é: ', soma)
