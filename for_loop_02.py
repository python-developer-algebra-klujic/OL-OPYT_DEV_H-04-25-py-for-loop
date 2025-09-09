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
for number in range(height):
    print('*' + ' ' * number + '*')

print('*' + '*' * height + '*')
print()
print()