from time import sleep

def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0:
        c = 1
    if a > b:
        c = c - (c * 2)
        b -= 1
    if b > a:
        b += 1
    for d in range(a, b, c):
        print(f'{d} ', end='')
        sleep(0.2)
    print('FIM')
    
n1=int(input('Você quer contar a partir de qual número? '))
n2=int(input('Qual será o número final? '))
n3=int(input('De quantos em quantos números é pra ser contado? '))
contador(n1, n2, n3)
