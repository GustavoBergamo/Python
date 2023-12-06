#ler duas notas, calcular média até 5 reprovado, entre 5 e 6.9 recuperação ou aprovado
n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda  nota? '))
r = (n1 + n2) / 2
if r <= 5:
    print('Sua média foi {:.2f} e você está'.format(r))
    print('\033[7;31mREPROVADO\033[m')
elif r > 5 and r < 6.9:
    print('Sua média foi {:.2f} e você está'.format(r))
    print('\033[7;37mDE RECUPERAÇÃO\033[m')
elif r >= 7:
    print('Sua média foi {:.2f} e você está'.format(r))
    print('\033[7;36mAPROVADO\033[m')