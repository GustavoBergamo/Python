#56 ler nome, idade e sexo de 4 pessoas, mostrar média de idade
#homem mais velho e quantas mulheres tem menos de 20 anos
somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
mulheres = 0
for p in range(1, 5):
    print('========={}========='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é {:.1f}'.format(mediaidade))
print('O mais velho é {} e tem {} anos'.format(nomevelho, maioridade))
print('E {} mulheres tem menos de 20 anos'.format(mulheres))