while True:
    t = int(input('tabuada qual numero? '))
    if t < 0:
        break
    for c in range (1, 11):
        print(f'{t}x{c}={t * c}')
        c += 1
print('fim')