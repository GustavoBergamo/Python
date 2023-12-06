#ler ano de nascimento, informar idade, se vai se alistar, se é hora de alistar
#ou se já passou do tempo. Informar quanto tempo falta ou já passou
from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
hoje = date.today().year
r = hoje - ano
print('Você tem {} anos'.format(r))
if r < 18:
    print('Faltam {} anos para se alistar'.format(18 - r))
elif r == 18:
    print('Você deve se alistar este ano')
elif r > 18:
    print('Já se passaram {} ano(s) do seu alistamento'.format(r - 18))
print('Tenha um bom dia')