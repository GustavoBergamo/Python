from time import sleep
def contador(a, b, c):
    print('=-' * 20)
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
    print('=-' * 20)
