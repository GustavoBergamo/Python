#ler data de nascimento e categorizar até 9 anos mirim, 14 infantil, 19 junior, 20 senior e mais master
import datetime
nasc = int(input('Qual seu ano de nascimento? '))
hoje = datetime.date.today()
r = (hoje.year - nasc)
print(r, 'anos')
if r <= 9:
    print('Mirim')
elif r > 9 and r <= 14:
    print('Infantil')
elif r > 14 and r <= 19:
    print('Junior')
elif r > 19 and r <=20:
    print('Sênior')
elif r > 20:
    print ('Master')