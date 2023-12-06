#ler peso e altura e calcular imc
p = int(input('Qual seu peso em kg? '))
a = int(input('Qual sua altura em cm? '))
imc = p / ((a / 100) * (a / 100))
print('Seu imc é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')