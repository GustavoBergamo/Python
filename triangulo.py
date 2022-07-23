#refazer ex 25 dizendo se será equilátero, isósceles ou escaleno
print('Vou descobrir se 3 retas podem formar um triângulo')
a = int(input('\033[31mDigite o tamanho da primeira reta: '))
b = int(input('Digite o tamanho da segunda reta: '))
c = int(input('Agora o tamanho da terceira reta: '))
print('\033[m---'*12)
print('\033[7mAtendendo as seguintes condições\033[m')
print((a - b), '<', c, '<', (a + b))
print((a - c), '<', b, '<', (a + c))
print((b - c), '<', a, '<', (b + c))
print('\033[m---'*12)
if (a-b) < c < (a+b) and (a-c) < b < (a+c) and (b-c) < a < (b+c):
    print('\033[4;33mÉ possível formar um triângulo com essas retas')
    if a == b and b == c:
        print('equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('\033[4;33mNão é possível formar um triângulo com essas retas')