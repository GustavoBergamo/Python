#Ler velocidade do carro
#se > 80 km foi multado
#a multa custa 7 reais por cada km acima do limite

vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você excedeu a velocidade e a multa será de R${}'.format((vel-80)*7))
else:
    print('Parabéns por manter a velocidade no limite')