#ler numero inteiro e usuario escolhe se converte pra binario, octal ou hexadecimal
n = int(input('digite um numero: '))
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
op = int(input('opcão: '))
if op == 1:
    print('binario: {}'.format(bin(n)[2:]))
elif op == 2:
    print('octal: {}'.format(oct(n)[2:]))
elif op == 3:
    print('hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('opção inválida!')