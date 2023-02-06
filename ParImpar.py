from random import randint

while True:
    jogador = 0
    pi = 3
    n = 11
    computador = randint(0, 10)
    while True:
        if pi != 1 or pi != 2:
            pi = int(input('[1] Par ou [2] impar '))
        if pi == 1 or pi == 2:
            break
    while True:
        if n < 0 or n > 10:
            n = int(input('Qual seu número entre 0 e 10? '))
        if n >= 0 and n <= 10:
            break
    r = (computador + n) % 2
    if pi == 1 and r == 0:
        print(f'coloquei {computador} e você {n}, como escolheu Par')
        print('GANHOU')
    if pi == 2 and r != 0:
        print(f'coloquei {computador} e você {n}, como escolheu Impar')
        print('GANHOU')
    if pi == 1 and r != 0:
        print(f'coloquei {computador} e você {n}, como escolheu Par')
        print('PERDEU')
        break
    if pi == 2 and r == 0:
        print(f'coloquei {computador} e você {n}, como escolheu Impar')
        print('PERDEU')
        break
print ('Fim do jogo')
