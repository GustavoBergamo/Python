#Ver se aprova empréstimo, ver valor da casa, salario e quantos anos pra pagar
#a prestação não pode exceder 30% do salário senão vai negar
print('\033[7mPrograma para viabilidade de empréstimo\033[m')
casa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual o seu salário atual? R$'))
ano = int(input('Em quantos anos você quer pagar o emprestimo? '))
prestacao = (casa / (ano * 12))
if prestacao < (salario * 0.3):
    print('Aprovado! Serão {} parcelas de R${:.2f}'.format((ano * 12), prestacao))
else:
    print('\033[33mNegado!')