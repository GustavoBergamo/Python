from turtle import clear
n1 = 0
soma = 1
c = 1
quantos = int(input('Quantos números da sequencia de Fibonacci você quer ver? '))
print('1>', end='')
while c != quantos:
    c += 1
    soma += n1
    n1 = soma - n1
    print(soma, end='>')
print('fim')