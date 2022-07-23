n1=float(input('qual a altura da parede? '))
n2=float(input('qual a largura? '))
a=n1*n2
t=(a//2)+1
print ('a parede tem {:.2f} m2 e precisa de {:.0f} litros de tinta para pintá-la'.format(a,t))