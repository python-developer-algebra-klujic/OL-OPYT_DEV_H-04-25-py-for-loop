'''
Napisite program koji ispisuje trokut tako da su linije stranica prikazane zvjezdicama *.

*
**
* *
*  *
*   *
*    *
*******
'''
print('Ispis trokuta fiksne visine bez for petlje')
print('*')
print('**')
print('* *')
print('*  *')
print('*   *')
print('*    *')
print('*******')
print()
print()









print('Ispis trokuta fiksne visine pomocu for petlje')
print('*')

for number in range(5):
    print('*' + ' ' * number + '*')

print('*******')
print()
print()












print('Ispis trokuta varijabilne visine pomocu for petlje')

height = int(input('Unesite visinu trokuta: '))

print('*')
for number in range(height - 2):
    # print('*' + ' ' * number + '*')
    print(f'*{" " * number}*')

# print('*' + '*' * (height - 2) + '*')
print(f'{"*" * (height)}')
print()
print()















print('Ispis trokuta varijabilne visine pomocu for petlje')
print('uz izbor znaka za iscrtavanje linija strnica trokuta')

height = int(input('Unesite visinu trokuta: '))
symbol = input('Unesite znak za iscrtavanje stranica trokuta: ')

print(symbol)
for number in range(height - 2):
    print(f'{symbol}{" " * number}{symbol}')

print(f'{symbol * (height)}')
print()
print()
