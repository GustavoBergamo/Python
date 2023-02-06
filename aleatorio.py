#Numero aleatório entre 0 e 10 inteiro
#o usuário tentará descobrir em quantas vezes e dizer quantas tentativas foram
import random
n = int(input('Tente advinhar o número que estou pensando entre 0 e 10: '))
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 1
random.shuffle(m)
#poderia ser também m = randint(0, 10)
while n is not m[0]:
    print('errado')
    if n < m[0]:
        print('É maior')
    else:
        print('É menor')
    c += 1
    n = int(input('Tente novamente: '))
print('Eu pensei no {}. Você advinhou em {} tentativas'.format(m[0], c))