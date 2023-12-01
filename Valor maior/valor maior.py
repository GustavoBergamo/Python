def maior(lst):
    resultado = 0
    for c in lst:
        if c > resultado:
            resultado = c
    print(f'O valor maior é: {resultado}')


print('Digite os números (999 termina): ')
num = []
a = 0
while True:
    a = int(input('=> '))
    if a == 999:
        break
    num.append(a)
print(num)
maior(num)
