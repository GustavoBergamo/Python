#Programa que joga pedra, papel, tesoura
from time import sleep
print('''
+-----------------+
| VAMOS JOGAR PPT |
+-----------------+

[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
itens = ['PEDRA', 'PAPEL', 'TESOURA']
j = int(input('\033[7mFaça sua escolha => \033[m'))
from random import randint
c = randint(0, 2)
print('Você jogou......: {}'.format(itens[j]))
print('                    X')
sleep (2)
print('Computador jogou: {}'.format(itens[c]))
if j == 0 and c == 0:
    print('empate')
elif j == 0 and c == 1:
    print('(ganhei)')
elif j == 0 and c == 2:
    print('(perdi)')
elif j == 1 and c == 0:
    print('(ganhou)')
elif j == 1 and c == 1:
    print('(empate)')
elif j == 1 and c == 2:
    print('(ganhei)')
elif j == 2 and c == 0:
    print('(ganhei)')
elif j == 2 and c == 1:
    print('(ganhou)')
elif j == 2 and c == 2:
    print('(empate)')
else:
    print ('opção errada')
