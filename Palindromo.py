#Ler uma frase e dizer se é palindromo
frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto)
print(inverso)
if junto == inverso:
    print('é um palíndromo')
else:
    print('não é')