#Calcular valor do produto considerando preço e condição de pagamento
p = int(input('Qual o valor do produto? R$'))
print('\033[32mEscolha a condição de pagamento:\033[m')
print('''[1] à vista em dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
o = int(input('=> '))
if o == 1:
    r = p * 0.9
    print('O valor final é de R${:.2f}'.format(r))
elif o == 2:
    r = p * 0.95
    print('O valor final é de R${:.2f}'.format(r))
elif o == 3:
    r = p
    print('O valor final é de R${:.2f}'.format(r))
elif o == 4:
    r = p * 1.2
    print('O valor final é de R${:.2f}'.format(r))
else:
    print('opção incorreta')